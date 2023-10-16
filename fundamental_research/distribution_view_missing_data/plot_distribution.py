import glob
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



files = glob.glob('results/*.csv')
#print(files)



def get_ideal_utility_score(path_file_ideal, view_name):
	df = pd.read_csv(path_file_ideal)
	utility = df.loc[df['view'] == view_name, 'utility'].values
	return utility[0]





df = pd.read_csv('distribution/30.csv')
#print(df.head())



# utility_ideal_thal_oldpeak_sum = get_ideal_utility_score('results/ideal_views.csv', 'thal_oldpeak_sum')
# print(utility_ideal_thal_oldpeak_sum)

# thal_oldpeak_sum = df['thal_oldpeak_sum']
# thal_oldpeak_sum = thal_oldpeak_sum.dropna()

# plt.hist(thal_oldpeak_sum)
# plt.title("thal_oldpeak_sum, utility ideal = {}".format(utility_ideal_thal_oldpeak_sum))
# plt.axvline(utility_ideal_thal_oldpeak_sum, color='#fc7303', linestyle='dashed', linewidth=3)
# plt.show()

#print(result)



new_df = df.iloc[:,[1,2,3,4,5,6,7,8,9,10]]
new_df = new_df.dropna()
new_df.hist()