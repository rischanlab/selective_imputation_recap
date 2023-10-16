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



mean0 = df[df['measurement'] == 'VizPut-Ranking-Aware-Inverted-U'].reset_index()
mean0 = mean0['mean']
ub0 = df[df['measurement'] == 'VizPut-Ranking-Aware-Inverted-U'].reset_index()
ub0 = ub0['ub']
lb0 = df[df['measurement'] == 'VizPut-Ranking-Aware-Inverted-U'].reset_index()
lb0 = lb0['lb']

mean1 = df[df['measurement'] == 'VizPut-Ranking-Aware-Importance-Gap'].reset_index()
mean1 = mean1['mean']
ub1 = df[df['measurement'] == 'VizPut-Ranking-Aware-Importance-Gap'].reset_index()
ub1 = ub1['ub']
lb1 = df[df['measurement'] == 'VizPut-Ranking-Aware-Importance-Gap'].reset_index()
lb1 = lb1['lb']


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
ax.plot(mean0, lw = 1, color = '#b31270', alpha = 1, label = 'VizPut-Ranking-Aware-Inverted-U',  marker='*', linestyle='--', linewidth=2, markersize=20)
ax.plot(mean1, lw = 1, color = '#2596be', alpha = 1, label = 'VizPut-Ranking-Aware-Importance-Gap', marker='+', linestyle='-.', linewidth=2, markersize=20)

# Shade the confidence interval
ax.fill_between(t, lb0, ub0, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb1, ub1, color = '#dedddc', alpha = 0.4)




# Label the axes and provide a title
#ax.set_title("Impact of k on Effectiveness, 95% CI, 10 % A missing")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness")
x = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]
xi = list(range(len(x)))
plt.xticks(xi[::2], x[::2]) # Skip every other tick
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()
