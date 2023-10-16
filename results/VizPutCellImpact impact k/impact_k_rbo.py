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

input_file = 'data/rbo.csv'

output_plot = 'impact_k_pbci_rbo'

# ===============================================================
# IDEAL VS STANDARD



df = pd.read_csv(input_file, names=['k','measurement','mean','lb','ub'])



mean0 = df[df['measurement'] == 'No Imputation'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'No Imputation'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'No Imputation'].reset_index()
lb0 = lb0['lb']

mean1 = df[df['measurement'] == 'VizPut-Cell-Impact'].reset_index()
mean1 = mean1['mean']
ub1 = df[df['measurement'] == 'VizPut-Cell-Impact'].reset_index()
ub1 = ub1['ub']
lb1 = df[df['measurement'] == 'VizPut-Cell-Impact'].reset_index()
lb1 = lb1['lb']

mean2 = df[df['measurement'] == 'RandomSelectionImputation'].reset_index()
mean2 = mean2['mean']
ub2 = df[df['measurement'] == 'RandomSelectionImputation'].reset_index()
ub2 = ub2['ub']
lb2 = df[df['measurement'] == 'RandomSelectionImputation'].reset_index()
lb2 = lb2['lb']

mean3 = df[df['measurement'] == 'VizPut-Cell-Impact-Fairness'].reset_index()
mean3 = mean3['mean']
ub3 = df[df['measurement'] == 'VizPut-Cell-Impact-Fairness'].reset_index()
ub3 = ub3['ub']
lb3 = df[df['measurement'] == 'VizPut-Cell-Impact-Fairness'].reset_index()
lb3 = lb3['lb']

mean4 = df[df['measurement'] == 'Fairness Imputation'].reset_index()
mean4 = mean4['mean']
ub4 = df[df['measurement'] == 'Fairness Imputation'].reset_index()
ub4 = ub4['ub']
lb4 = df[df['measurement'] == 'Fairness Imputation'].reset_index()
lb4 = lb4['lb']

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


t = np.arange(len(mean0))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean0, lw = 1, color = '#000000', alpha = 1, label = 'No imputation', marker='x', linestyle=':', linewidth=2, markersize=20)
ax.plot(mean2, lw = 1, color = '#008000', alpha = 1, label = 'Random selection imputation', marker='o', linestyle='--', linewidth=2, markersize=20)
ax.plot(mean1, lw = 1, color = '#FF0000', alpha = 1, label = 'VizPut-Cell-Impact', marker='<', linestyle='-', linewidth=2, markersize=20)
ax.plot(mean3, lw = 1, color = '#0000FF', alpha = 1, label = 'VizPut-Cell-Impact-Fairness', marker='*', linestyle=':', linewidth=2, markersize=20)
ax.plot(mean4, lw = 1, color = '#990000', alpha = 1, label = 'Fairness imputation', marker='s', linestyle='-.', linewidth=2, markersize=20)

# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb1, ub1, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb4, ub4, color = '#dedddc', alpha = 0.4)




# Label the axes and provide a title
#ax.set_title("Impact of k on Effectiveness, 95% CI, 10 % A missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness")
x = [5, 10, 20, 30, 40]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
