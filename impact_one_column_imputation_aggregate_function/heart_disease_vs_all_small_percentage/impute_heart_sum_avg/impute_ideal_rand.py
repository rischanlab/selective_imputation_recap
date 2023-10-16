import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
import csv
import sys
import sqldf
from collections import defaultdict
from math import log,pi
from decimal import Decimal
import timeit
import math
import rbo_func as rbo


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
        q2="select "+a+", "+f+"("+m+") from df_param_passing where "+a+" is not null group by "+a+" order by "+a+";"
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

# Function for put missing random

def dropout(a, percent, seed):
    # create a copy
    mat = a.copy()
    # number of values to replace
    prop = int(mat.size * percent)
    # indices to mask
    random.seed(seed)
    mask = random.sample(range(mat.size), prop)
    # replace with NaN
    np.put(mat, mask, [np.NaN]*len(mask))
    return mat

def missing_data(db, percentage, seed):
    df = db.copy()
    data = df.values
    modified = dropout(data, percentage, seed)
    new_df = pd.DataFrame(modified) #Change % of data to NA in the dataset
    columns = ['age', 'sex', 'cp', 'restbp', 'chol', 'fbs', 'restecg', 'thalach',
       'exang', 'oldpeak', 'slope', 'ca', 'thal']
    new_df.columns = columns
    return new_df


continuous=['age', 'restbp', 'chol', 'thalach', 'ca', 'oldpeak']
discrete=['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']
aggregate= ['sum','avg']#,'max']

# Code Body

df = pd.read_csv('heart.csv')

#print(df)

k_list = [5,10,15,20,25]
mlist = [0,0.05,0.1,0.15,0.2]

for k in k_list:
    ideal_topk  = generate_topk_views(k, df)
    sum_ideal = get_utility_score_ideal_topk(k, ideal_topk)

    unique_ideal = get_unique(k, ideal_topk)
    unique_col = [ item for elem in unique_ideal for item in elem]
    for i in mlist:
        for j in range(100):
            df1 = df.copy()
            df1.drop(['num'], axis=1, inplace=True)
            data = missing_data(df1, i, j)
            data['num'] = df['num']

            random.seed(j)
            col_rand = random.sample(df.columns.tolist(), len(unique_col))
            # [['thal', 'cp', 'slope'], ['oldpeak', 'thalach', 'restbp', 'ca']]

            for col in col_rand:
                data.drop([col], axis=1, inplace=True)
                data[col] = df[col]

            #print(data)
            missing_topk = generate_topk_views(k, data)
            sum_missing = get_utility_score_missing_topk(k, ideal_topk, missing_topk)
            with open('results/sumavg_ideal_rand_impute.csv', 'a', newline='') as f:
                #print(missing_topk, len(missing_topk))
                #print(topk, len(topk))
                fields = [i*100, k, rboresult(missing_topk, ideal_topk), jaccard_similarity(missing_topk, ideal_topk), cum_score(sum_missing,sum_ideal)]
                print(fields)
                writer = csv.writer(f)
                writer.writerow(fields)
