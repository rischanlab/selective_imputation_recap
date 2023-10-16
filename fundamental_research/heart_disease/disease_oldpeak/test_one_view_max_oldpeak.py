import sys
import random
import sqldf
import pandas as pd
import numpy as np
import math
import csv


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
    new_df = pd.DataFrame(modified)  #Change % of data to NA in the dataset
    columns = ['num','oldpeak']
    new_df.columns = columns
    return new_df

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

def get_query_result( query ) :
    df_view = sqldf.run(query)
    return df_view



df=pd.read_csv('heart.csv')
df=pd.read_csv('heart.csv')
df = df[['num','oldpeak','cp']]

mlist = [0,0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.6, 0.7] 

for i in mlist:
	for j in range(100):
		df1 = df.copy()
		df1.drop(['cp'], axis=1, inplace=True)
		di1 = missing_data(df1, i, j)
		di1['cp'] = df['cp']

		q1="select num, max(oldpeak) from df where cp = 'typical_angina' and num is not null group by num order by num;"
		q2="select num, max(oldpeak) from di1 where cp = 'typical_angina' and num is not null group by num order by num;"


		res_1=get_query_result(q1)
		res_1.columns = ['heart_disease','max_oldpeak']
		res_1['max_oldpeak'] = res_1['max_oldpeak']/sum(res_1['max_oldpeak'])
		res_1 = res_1.set_index('heart_disease')
		res_2=get_query_result(q2)
		res_2.columns = ['heart_disease','max_oldpeak']
		res_2['max_oldpeak'] = res_2['max_oldpeak']/sum(res_2['max_oldpeak'])
		res_2 = res_2.set_index('heart_disease')


		dist = 1 - get_utility(res_1['max_oldpeak'],res_2['max_oldpeak'])
		with open('results/max_oldpeak_distance.csv', 'a', newline='') as f:
			fields = [i*100, dist]
			print(fields)
			writer = csv.writer(f)
			writer.writerow(fields)
