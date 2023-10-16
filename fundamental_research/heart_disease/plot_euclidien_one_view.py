import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.stats

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

input_file1 = 'results/distance_avg.csv'
input_file2 = 'results/distance_max.csv'





output_plot = 'distance'


# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file1, names=['percentage','dist'])
df = df.dropna()

dfj100 = df[(df['percentage'] == 0)]
dfj100 = dfj100['dist']

dfj110 = df[(df['percentage'] == 5)]
dfj110 = dfj110['dist']

dfj120 = df[(df['percentage'] == 10)]
dfj120 = dfj120['dist']

dfj130 = df[(df['percentage'] == 15)]
dfj130 = dfj130['dist']

dfj140 = df[(df['percentage'] == 20)]
dfj140 = dfj140['dist']

dfj150 = df[(df['percentage'] == 25)]
dfj150 = dfj150['dist']

dfj160 = df[(df['percentage'] == 30)]
dfj160 = dfj160['dist']







dfj100 = list(mean_confidence_interval(dfj100))
dfj100.insert(0,0)
dfj100.insert(1,'dist')

dfj110 = list(mean_confidence_interval(dfj110))
dfj110.insert(0,5)
dfj110.insert(1,'dist')

dfj120 = list(mean_confidence_interval(dfj120))
dfj120.insert(0,10)
dfj120.insert(1,'dist')

dfj130 = list(mean_confidence_interval(dfj130))
dfj130.insert(0,15)
dfj130.insert(1,'dist')

dfj140 = list(mean_confidence_interval(dfj140))
dfj140.insert(0,20)
dfj140.insert(1,'dist')

dfj150 = list(mean_confidence_interval(dfj150))
dfj150.insert(0,25)
dfj150.insert(1,'dist')

dfj160 = list(mean_confidence_interval(dfj160))
dfj160.insert(0,30)
dfj160.insert(1,'dist')


df = pd.read_csv(input_file2, names=['percentage','dist'])
df = df.dropna()


dfj200 = df[(df['percentage'] == 0)]
dfj200 = dfj200['dist']

dfj210 = df[(df['percentage'] == 5)]
dfj210 = dfj210['dist']

dfj220 = df[(df['percentage'] == 10)]
dfj220 = dfj220['dist']

dfj230 = df[(df['percentage'] == 15)]
dfj230 = dfj230['dist']

dfj240 = df[(df['percentage'] == 20)]
dfj240 = dfj240['dist']

dfj250 = df[(df['percentage'] == 25)]
dfj250 = dfj250['dist']

dfj260 = df[(df['percentage'] == 30)]
dfj260 = dfj260['dist']

# dfj270 = df[(df['percentage'] == 70)]
# dfj270 = dfj270['Cumulative_distance']



dfj200 = list(mean_confidence_interval(dfj200))
dfj200.insert(0,0)
dfj200.insert(1,'dist')

dfj210 = list(mean_confidence_interval(dfj210))
dfj210.insert(0,5)
dfj210.insert(1,'dist')

dfj220 = list(mean_confidence_interval(dfj220))
dfj220.insert(0,10)
dfj220.insert(1,'dist')

dfj230 = list(mean_confidence_interval(dfj230))
dfj230.insert(0,15)
dfj230.insert(1,'dist')

dfj240 = list(mean_confidence_interval(dfj240))
dfj240.insert(0,20)
dfj240.insert(1,'dist')

dfj250 = list(mean_confidence_interval(dfj250))
dfj250.insert(0,25)
dfj250.insert(1,'dist')

dfj260 = list(mean_confidence_interval(dfj260))
dfj260.insert(0,30)
dfj260.insert(1,'dist')

# dfj270 = list(mean_confidence_interval(dfj270))
# dfj270.insert(0,70)
# dfj270.insert(1,'Cumulative_distance')


df1 = pd.DataFrame([dfj100, dfj110, dfj120, dfj130, dfj140, dfj150, dfj160])#, dfj190])
df1.columns = ['percentage','measurement','mean','lb','ub']
df2 = pd.DataFrame([dfj200, dfj210, dfj220, dfj230, dfj240, dfj250, dfj260])#, dfj290])
df2.columns = ['percentage','measurement','mean','lb','ub']
#print(df1)



mean1 = df1[df1['measurement'] == 'dist'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'dist'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'dist'].reset_index()
lb1 = lb1['lb']

mean2 = df2[df2['measurement'] == 'dist'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'dist'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'dist'].reset_index()
lb2 = lb2['lb']

# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (15, 9))
# Font size to 14
matplotlib.rc('font', size = 25)
# Do not display top and right frame lines
matplotlib.rc('axes.spines', top = False, right = False)
# Remove grid lines
matplotlib.rc('axes', grid = False)
# Set backgound color to white
matplotlib.rc('axes', facecolor = 'white')


#print(mean1)

t = np.arange(len(mean1))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean1, lw = 1, color = '#fc7303', alpha = 1, label = 'disease_avg_oldpeak', marker='x', linestyle=':', linewidth=2, markersize=20)
ax.plot(mean2, lw = 1, color = '#FF0000', alpha = 1, label = 'restecg_max_chol', marker='<', linestyle='-.', linewidth=2, markersize=20)
# ax.plot(mean3, lw = 1, color = '#008000', alpha = 1, label = 'Dirty impute', marker='o', linestyle='--', linewidth=2, markersize=20)
# ax.plot(mean4, lw = 1, color = '#0000FF', alpha = 1, label = 'No Impute', marker='+', linestyle=':', linewidth=2, markersize=20)
# # ax.plot(mean5, lw = 1, color = '#800000', alpha = 1, label = 'Num of Suicides', marker='*', linestyle='-', linewidth=2, markersize=20)
# # ax.plot(mean6, lw = 1, color = '#3e6980', alpha = 1, label = 'Suicides per 100k Pop', marker='>', linestyle='-.', linewidth=2, markersize=20)
# # ax.plot(mean7, lw = 1, color = '#000000', alpha = 1, label = 'No Impute', marker='s', linestyle='--', linewidth=2, markersize=20)



# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#dedddc', alpha = 0.4)
# ax.fill_between(t, lb3, ub3, color = '#dedddc', alpha = 0.4)
# ax.fill_between(t, lb4, ub4, color = '#dedddc', alpha = 0.4)
# # ax.fill_between(t, lb5, ub5, color = '#dedddc', alpha = 0.4)
# # ax.fill_between(t, lb6, ub6, color = '#dedddc', alpha = 0.4)
# # ax.fill_between(t, lb7, ub7, color = '#dedddc', alpha = 0.4)




# Label the axes and provide a title
#ax.set_title("Impact missing on Effectiveness (RBO), 95% CI, k = 10")
ax.set_xlabel("percentage of missing data")
ax.set_ylabel("Distance between viz of complete vs incomplete")
x = [0, 5, 10, 15, 20, 25, 30]#, 90]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=0.3)

ax.legend(frameon=False, loc='best')

plt.savefig(''+ output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('' + output_plot + '.png')
plt.show()
