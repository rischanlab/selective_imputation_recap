# -*- coding: utf-8 -*-
from a_seedb_function import SeeDB
from a_seedb_db import data
import psycopg2
conn = psycopg2.connect("dbname=temp_after_ideal_imputation2 user=postgres password=zenvisage")

cursor = conn.cursor()
cursor.execute("""SELECT table_name FROM information_schema.tables
       WHERE table_schema = 'public'""") # and table_name like '%diabetes%'
mytable_db = cursor.fetchall()


if __name__ == "__main__":

    top_k = 10
    #atr = ['race', 'gender', 'age']
    atr = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'thal']
    #measure = ['time_in_hospital', 'num_lab_procedures', 'num_procedures']
    measure = ['age', 'restbp', 'chol', 'thalach', 'ca', 'oldpeak']

    func = ['sum', 'avg', 'max']

    # for i in mytable:
    #     db, table, data_set = data(i[0], atr, measure, func)
    #     print("running with db {}".format(i[0]))
    #     framework = SeeDB(db,data_set,table,top_k)
    #     framework.main()
    #     print("done")
    # mlist = [0.8]
    # mytable = ['db6']
    # for i in mlist:
    #     for j in range(100):
    #         # print(int(i * 100), j)
    #         x = int(i * 100)
    #         # print(df)
    #         # print(df.columns.to_series().groupby(df.dtypes).groups)
    #         # db missing is db with row contains missing drop
    #         # db NaN is db with row contain missing keep
    #         #table_name1 = "db_" + str(x) + "rand_missing_attr" + str(j + 1)
    #         #table_name2 = "db_" + str(x) + "rand_missing_measure" + str(j + 1)
    #         table_name3 = "db_" + str(x) + "rand_missing_a_m" + str(j + 1)
    #         #mytable.append(table_name1)
    #         #mytable.append(table_name2)
    #         mytable.append(table_name3)
    # print(mytable)
    # print(len(mytable))

    for i in mytable_db:
            db, table, data_set = data(i[0], atr, measure, func)
            print("running with db {}".format(i[0]))
            try:
                framework = SeeDB(db, data_set, table, top_k)
                framework.main()
            except:
                pass  # doing nothing on exception
            print("done")