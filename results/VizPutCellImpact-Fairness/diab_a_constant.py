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



output_plot = 'diab_a_constant'



df1 = pd.read_csv('diab_a_constant/noimpute.csv')
df2 = pd.read_csv('diab_a_constant/pbci.csv') #PBCI
df3 = pd.read_csv('diab_a_constant/random_imputation.csv')
df4 = pd.read_csv('diab_a_constant/pbci_fairness.csv')
df5 = pd.read_csv('diab_a_constant/fairness.csv')


mean1 = df1[df1['measurement'] == 'RBO'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'RBO'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'RBO'].reset_index()
lb1 = lb1['lb']

mean2 = df2[df2['measurement'] == 'RBO'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'RBO'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'RBO'].reset_index()
lb2 = lb2['lb']

mean3 = df3[df3['measurement'] == 'RBO'].reset_index()
mean3 = mean3['mean']
ub3 = df3[df3['measurement'] == 'RBO'].reset_index()
ub3 = ub3['ub']
lb3 = df3[df3['measurement'] == 'RBO'].reset_index()
lb3 = lb3['lb']

mean4 = df4[df4['measurement'] == 'RBO'].reset_index()
mean4 = mean4['mean']
ub4 = df4[df4['measurement'] == 'RBO'].reset_index()
ub4 = ub4['ub']
lb4 = df4[df4['measurement'] == 'RBO'].reset_index()
lb4 = lb4['lb']

mean5 = df5[df5['measurement'] == 'RBO'].reset_index()
mean5 = mean5['mean']
ub5 = df5[df5['measurement'] == 'RBO'].reset_index()
ub5 = ub5['ub']
lb5 = df5[df5['measurement'] == 'RBO'].reset_index()
lb5 = lb5['lb']


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
ax.plot(mean2, lw = 1, color = '#FF0000', alpha = 1, label = 'VizPut-Cell-Impact', marker='<', linestyle='-.', linewidth=2, markersize=20)
ax.plot(mean4, lw = 1, color = '#0000FF', alpha = 1, label = 'VizPut-Cell-Impact-Fairness', marker='*', linestyle=':', linewidth=2, markersize=20)
ax.plot(mean5, lw = 1, color = '#990000', alpha = 1, label = 'Fairness imputation', marker='s', linestyle='-.', linewidth=2, markersize=20)
ax.plot(mean3, lw = 1, color = '#008000', alpha = 1, label = 'Random selection imputation', marker='o', linestyle='--', linewidth=2, markersize=20)
ax.plot(mean1, lw = 1, color = '#000000', alpha = 1, label = 'No imputation', marker='x', linestyle=':', linewidth=2, markersize=20)


# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb4, ub4, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb5, ub5, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#dedddc', alpha = 0.4)


# Label the axes and provide a title
#ax.set_title("Impact missing on Effectiveness - RBO, k = 10")
ax.set_xlabel("$|\mathbb{M}|$")
ax.set_ylabel("Effectiveness")
x = [1, 2, 3, 4, 5, 6,7,8,9,10,11,12]#, 35, 40]
xi = list(range(len(x)))
plt.xticks(xi, x)
ax.invert_yaxis()
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='best')
#plt.legend(prop={'size':18})
plt.legend(frameon=False)
plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
