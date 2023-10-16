import glob
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



files = glob.glob('results/*.csv')
#print(files)


def get_ideal_topk_views(k, df_path):
	df = pd.read_csv(df_path)
	topk = df.head(k)['view'].values
	return topk


def get_ideal_utility_score(path_file_ideal, view_name):
	df = pd.read_csv(path_file_ideal)
	utility = df.loc[df['view'] == view_name, 'utility'].values
	return utility[0]

def get_utility_score_single_view(path_files, view_name):
	# both params are strings 

	#path_files = 'results/30_*.csv'
	data = glob.glob(path_files)

	dist_view = []

	for i in data: 
		df = pd.read_csv(i)
		view = df.loc[df['view'] == view_name, 'utility'].values
		dist_view.append(view[0])
		# if math.isnan(float(view[0])) == False:
		# 	#print(view[0])
		# 	#dist_view.append(float("{:.3f}".format(view[0])))
		# 	dist_view.append(view[0])
	
	return dist_view




# thal_oldpeak_sum
# k = 10
# 30 % missing data

topk = get_ideal_topk_views(126, 'results/ideal_views.csv')


# 5% missing values 100 DB versions
df = pd.DataFrame([])
for i in topk:
	data = get_utility_score_single_view('results/5_*.csv',i)
	data = pd.Series(data)
	df[i] = data

print('Storing 5% missing data')
df.to_csv('distribution/5.csv', index=False)


# 10% missing values 100 DB versions
df = pd.DataFrame([])
for i in topk:
	data = get_utility_score_single_view('results/10_*.csv',i)
	data = pd.Series(data)
	df[i] = data

print('Storing 10% missing data')
df.to_csv('distribution/10.csv', index=False)


# 20% missing values 100 DB versions
df = pd.DataFrame([])
for i in topk:
	data = get_utility_score_single_view('results/20_*.csv',i)
	data = pd.Series(data)
	df[i] = data

print('Storing 20% missing data')
df.to_csv('distribution/20.csv', index=False)



# 30% missing values 100 DB versions
df = pd.DataFrame([])
for i in topk:
	data = get_utility_score_single_view('results/30_*.csv',i)
	data = pd.Series(data)
	df[i] = data
print('Storing 30% missing data')
df.to_csv('distribution/30.csv', index=False)



# 40% missing values 100 DB versions
df = pd.DataFrame([])
for i in topk:
	data = get_utility_score_single_view('results/40_*.csv',i)
	data = pd.Series(data)
	df[i] = data
print('Storing 40% missing data')
df.to_csv('distribution/40.csv', index=False)








# utility_ideal_thal_oldpeak_sum = get_ideal_utility_score('results/ideal_views.csv', 'thal_oldpeak_sum')
# print(utility_ideal_thal_oldpeak_sum)

# thal_oldpeak_sum = get_utility_score_single_view('results/30_*.csv','thal_oldpeak_sum')


# thal_oldpeak_sum = np.array(thal_oldpeak_sum)
# thal_oldpeak_sum = thal_oldpeak_sum[~np.isnan(thal_oldpeak_sum)]
# print(thal_oldpeak_sum)

# plt.hist(thal_oldpeak_sum)
# plt.title("thal_oldpeak_sum, utility ideal = {}".format(utility_ideal_thal_oldpeak_sum))
# plt.axvline(utility_ideal_thal_oldpeak_sum, color='#fc7303', linestyle='dashed', linewidth=3)
# plt.show()

#print(result)



