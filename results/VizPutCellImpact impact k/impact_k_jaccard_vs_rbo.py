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

input_file_rbo = 'data/rbo.csv'
input_file_jaccard = 'data/jaccard.csv'


output_plot = 'impact_k_pbci_jaccard_vs_rbo'

# ===============================================================
# IDEAL VS STANDARD



dfr = pd.read_csv(input_file_rbo, names=['k','measurement','mean','lb','ub'])
dfj = pd.read_csv(input_file_jaccard, names=['k','measurement','mean','lb','ub'])



mean0 = dfr[dfr['measurement'] == 'VizPut-Cell-Impact-Fairness'].reset_index()
mean0 = mean0['mean']
ub0 = dfr[dfr['measurement'] == 'VizPut-Cell-Impact-Fairness'].reset_index()
ub0 = ub0['ub']
lb0 = dfr[dfr['measurement'] == 'VizPut-Cell-Impact-Fairness'].reset_index()
lb0 = lb0['lb']

mean1 = dfj[dfj['measurement'] == 'VizPut-Cell-Impact-Fairness'].reset_index()
mean1 = mean1['mean']
ub1 = dfj[dfj['measurement'] == 'VizPut-Cell-Impact-Fairness'].reset_index()
ub1 = ub1['ub']
lb1 = dfj[dfj['measurement'] == 'VizPut-Cell-Impact-Fairness'].reset_index()
lb1 = lb1['lb']

# mean2 = df[df['measurement'] == 'PriorityBasedOnRandomSelection'].reset_index()
# mean2 = mean2['mean']
# ub2 = df[df['measurement'] == 'PriorityBasedOnRandomSelection'].reset_index()
# ub2 = ub2['ub']
# lb2 = df[df['measurement'] == 'PriorityBasedOnRandomSelection'].reset_index()
# lb2 = lb2['lb']

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
ax.plot(mean0, lw = 1, color = '#6b5005', alpha = 1, label = 'VizPut-Cell-Impact-Fairness - RBO', marker='x', linestyle=':', linewidth=2, markersize=20)
ax.plot(mean1, lw = 1, color = '#2e1fa1', alpha = 1, label = 'VizPut-Cell-Impact-Fairness - Jaccard', marker='<', linestyle='--', linewidth=2, markersize=10)
#ax.plot(mean2, lw = 1, color = '#008000', alpha = 1, label = 'PriorityBasedOnRandomSelection', marker='o', linestyle='--', linewidth=2, markersize=20)

# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb1, ub1, color = '#dedddc', alpha = 0.4)
#ax.fill_between(t, lb2, ub2, color = '#dedddc', alpha = 0.4)


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
