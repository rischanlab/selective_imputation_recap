# -*- coding: utf-8 -*-
import csv
import rbo_func as rbo
import glob
import sys
import random
import sqldf
import pandas as pd
import numpy as np
import seaborn as sns
from collections import defaultdict
from math import log,pi
from decimal import Decimal
import timeit
import math
import matplotlib.pyplot as plt


from scipy.spatial.distance import euclidean, chebyshev, cityblock, jaccard


# Functions get views and topk

def get_all_views():
    views=[]
    for f in aggregate:
        for a in discrete:
            for m in continuous:
                views.append((a,m,f))
    return views

def get_query_result( query ) :
    df_view = sqldf.run(query)
    return df_view

def normalize(f_list_1,f_list_2):
    f_list_1=[float(x) for x in f_list_1]
    f_list_2=[float(x) for x in f_list_2]
    sum_1=sum(f_list_1)
    sum_2=sum(f_list_2)
    norm_1 = [i/sum_1 for i in f_list_1]
    norm_2=[i/sum_2 for i in f_list_2]
    return norm_1,norm_2

def get_utility(f_list_1,f_list_2):
    nf_1,nf_2=normalize(f_list_1,f_list_2)
    #return kl.entropy(nf_1,nf_2)
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(nf_1, nf_2)]))
    return distance

def generate_topk_views(k, data):
    global df_param_passing
    df_param_passing = data
    dict_kl=defaultdict(list)
    views=get_all_views()
    #print(views)
    #runtime = []
    for a,m,f in views:
        #print (a,f,m)
        q1="select "+a+", "+f+"("+m+") from df_param_passing where num = 'disease' and "+a+" is not null group by "+a+" order by "+a+";"
        q2="select "+a+", "+f+"("+m+") from df_param_passing where num = 'no_disease' and "+a+" is not null group by "+a+" order by "+a+";"
        #print(q1)
        #startTime = timeit.default_timer()
        res_1=get_query_result(q1)
        res_2=get_query_result(q2)
        #stopTime = timeit.default_timer()
        #runtime.append(stopTime-startTime)
        f_list_1 = get_agg_values(res_1)
        f_list_2 = get_agg_values(res_2)
        dict_kl[a,m,f].append(get_utility(f_list_1,f_list_2))
        #print(f_list_1)

    #print(sum(runtime))
    temp = get_top_k(dict_kl, k)
    topk = get_topk(temp, k)
    return topk

def get_top_k(dict_kl, k):
    return sorted(dict_kl.items(), key= lambda item: item[1], reverse=True)[:k]

def get_agg_values(data):
    data.columns = ['a', 'b']
    #list_data = [data['b'][0], data['b'][1]]
    return data['b'].values.tolist()


def listToStringWithoutBrackets(list1):
    return str(list1).replace('[','').replace(']','')

def get_topk(data, k):
    topkdf = pd.DataFrame(data)
    topkdf.columns = ['view','utility']
    topkdf['id'] = range(1, len(topkdf) + 1)
    topkdf = topkdf.reindex(columns=sorted(topkdf.columns))
    topkdf['utility'] = topkdf['utility'].astype(str).apply(listToStringWithoutBrackets)
    topkdf['view'] = topkdf['view'].str.join('_')
    return topkdf.head(k)

def get_utility_score_ideal_topk(k, df):
    df = df.head(k)
    df['score'] = 1/np.log(df['id'] + 1) * df['utility'].astype(float)
    return df['score'].sum()

def get_utility_score_missing_topk(k, df_ideal, dirty):
    df2 = dirty.head(k)
    df2.drop(df2.columns[[0,1]], axis=1, inplace=True)
    df2 = df2.merge(df_ideal,on='view')
    df2.drop(df2.columns[[1]], axis=1, inplace=True)
    df2 = df2.reset_index()
    df2['id'] = df2.index + 1
    #print(df2)
    df2['score'] = 1/np.log(df2['id'] + 1) * df2['utility'].astype(float)
    score = df2['score'].sum()
    return score

def cum_score(sum_missing, sum_ideal):
    score = sum_missing/sum_ideal
    return score

def get_unique(k, df):
    df = df.head(k)
    df[['A', 'M', 'F']] = df['view'].str.split(pat='_', expand=True)
    a = df['A'].unique().tolist()
    #print("A",a)
    m = df['M'].unique().tolist()
    #print("M",m)
    #uniq = set(a + m)
    return [a,m]

def jaccard_similarity(dirty, ideal):
    dirty = dirty['view'].tolist()
    ideal = ideal['view'].tolist()
    s1 = set(dirty)
    #print(s1)
    s2 = set(ideal)
    #print(s2)
    return len(s1.intersection(s2)) / len(s1.union(s2))


def rboresult(ideal, dirty, p=0.95):
    dirty = dirty['view'].tolist()
    ideal = ideal['view'].tolist()

    return rbo.rbo(ideal, dirty, p)['ext']


continuous=['age', 'restbp', 'chol', 'thalach', 'oldpeak']
discrete=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal','ca']
aggregate= ['avg']


df=pd.read_csv('heart.csv')



if __name__ == "__main__":

    k_list = [5,10,15,20,25,30,35,40,45,50]

    

    for k in k_list:
        ideal_topk = generate_topk_views(k, df)
        print("Ideal topk", ideal_topk)
        num_samples = [30,40,50,60,70,80,90,100,150]
        for sample in num_samples:
            for i in range(50):
                # try:
                df_sample = df.sample(sample, random_state=i)
                sample_topk = generate_topk_views(k, df_sample)

                cum_ideal = get_utility_score_ideal_topk(k, ideal_topk)
                cum_sample = get_utility_score_missing_topk(k, ideal_topk, sample_topk)

                with open('results/100_seed_sample_vs_ideal.csv', 'a', newline='') as f:
                    fields = [sample, k, rboresult(ideal_topk, sample_topk), jaccard_similarity(sample_topk, ideal_topk), 
                    cum_score(cum_sample, cum_ideal)]
                    writer = csv.writer(f)
                    writer.writerow(fields)
                # except:
                #     pass  # doing nothing on exception
                # print("done")
