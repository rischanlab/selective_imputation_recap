# -*- coding: utf-8 -*-
import itertools


def data(table, atr, measure, func):
    db_name = 'temp_after_ideal_imputation2'
    table = table
    prod0 = list(itertools.product(func, measure))
    prod1 = [('count','*')]
    #print("prod",prod)
    prod = prod0 + prod1
    data_set = {i: prod for i in atr}
    
    return db_name,table,data_set

if __name__ == '__main__':
    print(00)

# A = 34
# M = 8
# F = 3
# 816 views



