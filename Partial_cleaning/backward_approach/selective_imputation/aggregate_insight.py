import csv
import rbo_func as rbo
import pandas as pd
from pandas import read_excel
import glob
import math
import numpy as np


def rboresult(groundtruth, new, p=0.95):
    return rbo.rbo(groundtruth, new, p)['ext']


def jaccard_similarity(list1, list2):
    s1 = set(list1)
    s2 = set(list2)
    return len(s1.intersection(s2)) / len(s1.union(s2))

def convert_to_one(item):
    S = []
    for i in item:
        S.append(((''.join(i))))
    return S


def get_topk_aggregate(k, file):
    my_sheet = 'Sheet1'
    file_name = file  # name of your excel file
    df = read_excel(file_name, sheet_name=my_sheet)
    df.drop(df.columns[[0,4]], axis=1, inplace=True)
    df = df.drop(df[df.Attributes == 'num'].index)
    df = df.head(k).values.tolist()
    x = convert_to_one(df)
    return x # shows headers with top 5 rows

def get_sim_topk_aggregate(k, file):
    my_sheet = 'Sheet1'
    file_name = file  # name of your excel file
    df = read_excel(file_name, sheet_name=my_sheet)
    df.drop(df.columns[[0,4]], axis=1, inplace=True)
    df = df.drop(df[df.Attributes == 'num'].index)
    df = df[::-1]
    df = df.head(k).values.tolist()
    x = convert_to_one(df)
    return x

def get_topk_variance(k, file):
    my_sheet = 'Sheet1'
    file_name = file  # name of your excel file
    df = read_excel(file_name, sheet_name=my_sheet)
    df = df.drop(df[df.Attributes == 'readmitted'].index)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df = df.head(k)
    var = df['Utility'].var()
    return var # shows headers with top 5 rows

def get_topk(k, file):
    df = pd.read_csv(file, index_col=0)
    df = df.head(k).values.tolist()
    x = convert_to_one(df)
    return x


def get_unique(k, file):
    df = pd.read_csv(file, index_col=0)
    df = df.head(k)
    uniq1 = df.level_0.unique().tolist()
    uniq2 = df.level_1.unique().tolist()
    uniq = set(uniq1 + uniq2)
    return list(uniq)

def generate_correlation_insights(data):
    dataCorr = data.corr(method='pearson')
    dataCorr = dataCorr[abs(dataCorr) >= 0.01].stack().reset_index()
    dataCorr = dataCorr[dataCorr['level_0'].astype(str) != dataCorr['level_1'].astype(str)]

    # filtering out lower/upper triangular duplicates
    dataCorr['ordered-cols'] = dataCorr.apply(lambda x: '-'.join(sorted([x['level_0'], x['level_1']])), axis=1)
    dataCorr = dataCorr.drop_duplicates(['ordered-cols'])
    dataCorr.drop(['ordered-cols'], axis=1, inplace=True)

    topk = dataCorr.sort_values(by=[0], ascending=False)
    topk = topk[['level_0', 'level_1']]
    # S = [item for sublist in topk_nomissing for item in sublist]
    topk = topk.reset_index()
    topk.drop(topk.columns[[0]], axis=1, inplace=True)
    return topk



## Cumulative Measurement 

def df_ideal(file):
    my_sheet = 'Sheet1'
    file_name = file  # name of your excel file
    df = read_excel(file_name, sheet_name=my_sheet)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df = df.drop(df[df.Attributes == 'num'].index)
    df['combined_col'] = df[['Attributes', 'Meassure', 'Function']].astype(str).apply(''.join, axis=1)
    df.drop(df.columns[[0,1,2]], axis=1, inplace=True)
    df = df[['combined_col','Utility']]
    df = df.reset_index()
    df['id'] = df.index + 1
    df = df[['id','combined_col','Utility']]
    return df


def get_utility_score_ideal_topk(k, df):
    df = df.head(k)
    df['score'] = 1/np.log(df['id'] + 1) * df['Utility']
    return df['score'].sum()

def get_utility_score_missing_topk(k, df_ideal, file2):
    #file2 = "db_70rand_missing_a_m74.xlsx"
    my_sheet = 'Sheet1'
    file_name = file2  # name of your excel file
    df2 = read_excel(file_name, sheet_name=my_sheet)
    df2.drop(df2.columns[[0,4]], axis=1, inplace=True)
    df2 = df2.drop(df2[df2.Attributes == 'num'].index)
    
    df2 = df2.head(k)
    df2['combined_col'] = df2[['Attributes', 'Meassure', 'Function']].astype(str).apply(''.join, axis=1)
    df2.drop(df2.columns[[0,1,2]], axis=1, inplace=True)
    df2 = df2.merge(df_ideal,on='combined_col')
    df2 = df2.reset_index()
    df2['id'] = df2.index + 1
    df2 = df2[['id','combined_col','Utility']]
    df2['score'] = 1/np.log(df2['id'] + 1) * df2['Utility']
    return df2['score'].sum()


def cum_score(sum_missing, sum_ideal):

    return sum_missing/sum_ideal

## Similarity

def df_ideal_sim(file):
    my_sheet = 'Sheet1'
    file_name = file  # name of your excel file
    df = read_excel(file_name, sheet_name=my_sheet)
    df.drop(df.columns[[0]], axis=1, inplace=True)
    df = df.drop(df[df.Attributes == 'num'].index)
    df['combined_col'] = df[['Attributes', 'Meassure', 'Function']].astype(str).apply(''.join, axis=1)
    df.drop(df.columns[[0,1,2]], axis=1, inplace=True)
    df = df[['combined_col','Utility']]
    df = df.reset_index()
    df['id'] = df.index + 1
    df = df[['id','combined_col','Utility']]
    df = df[::-1]
    df = df.reset_index()
    df['id'] = df.index + 1
    #df = df.sort_values(by=['Utility'], ascending=True)
    df['RealUtility'] = math.sqrt(2) - df['Utility']
    df = df[['id','combined_col','RealUtility']]
    return df

def get_utility_score_ideal_topk_sim(k, df):
    df = df.head(k)
    df['score'] = 1/np.log(df['id'] + 1) * df['RealUtility']
    return df['score'].sum()

def get_utility_score_missing_topk_sim(k, df_ideal, file2):
    #file2 = "db_70rand_missing_a_m74.xlsx"
    my_sheet = 'Sheet1'
    file_name = file2  # name of your excel file
    df2 = read_excel(file_name, sheet_name=my_sheet)
    df2.drop(df2.columns[[0,4]], axis=1, inplace=True)
    df2 = df2.drop(df2[df2.Attributes == 'num'].index)
    
    df2 = df2.tail(k)
    df2 = df2[::-1]
    df2['combined_col'] = df2[['Attributes', 'Meassure', 'Function']].astype(str).apply(''.join, axis=1)
    df2.drop(df2.columns[[0,1,2]], axis=1, inplace=True)
    df2 = df2.merge(df_ideal,on='combined_col')
    df2 = df2.reset_index()
    df2['id'] = df2.index + 1
    df2['score'] = 1/np.log(df2['id'] + 1) * df2['RealUtility']
    return df2['score'].sum()
