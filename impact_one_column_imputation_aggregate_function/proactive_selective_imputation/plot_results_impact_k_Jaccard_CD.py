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

input_file1 = 'results/dirty_impute.csv'
input_file2 = 'results/dirty_impute.csv'
# input_file3 = 'results/max_missing_vs_ideal.csv'
# input_file4 = 'results/max_ideal_impute.csv'
# input_file5 = 'results/suicides100kpop_impute.csv'
# input_file6 = 'results/suicidesno_impute.csv'
# input_file7 = 'results/missing_vs_ideal.csv'



output_plot = 'jaccard_cd_impact_m'

k = 3
percent = 50
# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file1, names=['percentage','k','m','RBO','Jaccard','Cumulative_distance'])

dfj100 = df[(df['k'] == k) & (df['percentage'] == percent)]
dfj100 = dfj100['Jaccard']

dfj110 = df[(df['k'] == k) & (df['percentage'] == percent)]
dfj110 = dfj110['Jaccard']

dfj120 = df[(df['k'] == k) & (df['percentage'] == percent)]
dfj120 = dfj120['Jaccard']

dfj130 = df[(df['k'] == k) & (df['percentage'] == percent)]
dfj130 = dfj130['Jaccard']

# dfj140 = df[(df['k'] == k) & (df['percentage'] == percent)]
# dfj140 = dfj140['Jaccard']

# dfj150 = df[(df['k'] == k) & (df['percentage'] == percent)]
# dfj150 = dfj150['Jaccard']

# dfj160 = df[(df['k'] == k) & (df['percentage'] == percent)]
# dfj160 = dfj160['Jaccard']

# dfj170 = df[(df['k'] == k) & (df['percentage'] == percent)]
# dfj170 = dfj170['Jaccard']





dfj100 = list(mean_confidence_interval(dfj100))
dfj100.insert(0,2)
dfj100.insert(1,'Jaccard')

dfj110 = list(mean_confidence_interval(dfj110))
dfj110.insert(0,3)
dfj110.insert(1,'Jaccard')

dfj120 = list(mean_confidence_interval(dfj120))
dfj120.insert(0,5)
dfj120.insert(1,'Jaccard')

dfj130 = list(mean_confidence_interval(dfj130))
dfj130.insert(0,10)
dfj130.insert(1,'Jaccard')

# dfj140 = list(mean_confidence_interval(dfj140))
# dfj140.insert(0,25)
# dfj140.insert(1,'Jaccard')

# dfj150 = list(mean_confidence_interval(dfj150))
# dfj150.insert(0,50)
# dfj150.insert(1,'Jaccard')

# dfj160 = list(mean_confidence_interval(dfj160))
# dfj160.insert(0,60)
# dfj160.insert(1,'Jaccard')

# dfj170 = list(mean_confidence_interval(dfj170))
# dfj170.insert(0,70)
# dfj170.insert(1,'Jaccard')

df = pd.read_csv(input_file2, names=['percentage','k','m','RBO','Jaccard','Cumulative_distance'])

dfc100 = df[(df['k'] == k) & (df['percentage'] == percent)]
dfc100 = dfc100['Cumulative_distance']

dfc110 = df[(df['k'] == k) & (df['percentage'] == percent)]
dfc110 = dfc110['Cumulative_distance']

dfc120 = df[(df['k'] == k) & (df['percentage'] == percent)]
dfc120 = dfc120['Cumulative_distance']

dfc130 = df[(df['k'] == k) & (df['percentage'] == percent)]
dfc130 = dfc130['Cumulative_distance']

# dfc140 = df[(df['k'] == k) & (df['percentage'] == percent)]
# dfc140 = dfc140['Cumulative_distance']

dfc100 = list(mean_confidence_interval(dfc100))
dfc100.insert(0,2)
dfc100.insert(1,'Cumulative_distance')

dfc110 = list(mean_confidence_interval(dfc110))
dfc110.insert(0,3)
dfc110.insert(1,'Cumulative_distance')

dfc120 = list(mean_confidence_interval(dfc120))
dfc120.insert(0,5)
dfc120.insert(1,'Cumulative_distance')

dfc130 = list(mean_confidence_interval(dfc130))
dfc130.insert(0,10)
dfc130.insert(1,'Cumulative_distance')


df1 = pd.DataFrame([dfj100, dfj110, dfj120, dfj130])#, dfj150, dfj160, dfj170])#, dfj190])
df1.columns = ['m','measurement','mean','lb','ub']

df2 = pd.DataFrame([dfc100, dfc110, dfc120, dfc130])#, dfc150, dfc160, dfc170])#, dfc190])
df2.columns = ['m','measurement','mean','lb','ub']


mean1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb1 = lb1['lb']

mean2 = df2[df2['measurement'] == 'Cumulative_distance'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'Cumulative_distance'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'Cumulative_distance'].reset_index()
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


t = np.arange(len(mean1))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean1, lw = 1, color = '#fc7303', alpha = 1, label = 'Jaccard', marker='x', linestyle=':', linewidth=2, markersize=20)
ax.plot(mean2, lw = 1, color = '#FF0000', alpha = 1, label = 'CD', marker='<', linestyle='-.', linewidth=2, markersize=20)



# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#dedddc', alpha = 0.4)




# Label the axes and provide a title
#ax.set_title("Impact missing on Effectiveness (RBO), 95% CI, k = 10")
ax.set_xlabel("m")
ax.set_ylabel("Effectiveness")
x = [2, 3, 5, 10]#, 25]#, 50, 60, 70, 90]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0)
ax.set_ylim(ymax=1.02)

ax.legend(frameon=False, loc='best')

plt.savefig(''+ output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('' + output_plot + '.png')
plt.show()
