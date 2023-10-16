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



output_plot = 'jaccard'

df1 = pd.read_csv('df1.csv') #avg_oldpeak
df2 = pd.read_csv('df2.csv') #max_oldpeak

df3 = pd.read_csv('df3.csv') #sum_oldpeak
# df4 = pd.read_csv('df4.csv') #avg_chol
# df5 = pd.read_csv('df5.csv') #avg_chol




mean1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb1 = lb1['lb']

mean2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
lb2 = lb2['lb']

mean3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
mean3 = mean3['mean']
ub3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
ub3 = ub3['ub']
lb3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
lb3 = lb3['lb']



# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (9, 9))
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
ax.plot(mean1, lw = 1, color = '#800000', alpha = 1, label = 'Ignore cells no imputation', marker='*', linestyle=':', linewidth=2, markersize=20)
ax.plot(mean2, lw = 1, color = '#0000FF', alpha = 1, label = 'Stratified selection imputation', marker='<', linestyle='-.', linewidth=2, markersize=20)
ax.plot(mean3, lw = 1, color = '#008000', alpha = 1, label = 'Uniform random selection imputation', marker='s', linestyle='--', linewidth=2, markersize=20)
#ax.plot(mean4, lw = 1, color = '#0000FF', alpha = 1, label = 'Similarity', marker='+', linestyle=':', linewidth=2, markersize=20)
#ax.plot(mean5, lw = 1, color = '#800000', alpha = 1, label = 'Outstanding', marker='*', linestyle='-', linewidth=2, markersize=20) 


# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#dedddc', alpha = 0.4)
#ax.fill_between(t, lb4, ub4, color = '#dedddc', alpha = 0.4)
#ax.fill_between(t, lb5, ub5, color = '#dedddc', alpha = 0.4)


# Label the axes and provide a title
#ax.set_title("Impact missing on Effectiveness (Jaccard), 95% CI, k = 10")
ax.set_xlabel("percentage of missing data")
ax.set_ylabel("Effectiveness")
x = [0, 5, 10, 15, 20, 25, 30]#, 90]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
