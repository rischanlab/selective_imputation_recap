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

input_file1 = '30_percent_missing.csv'
input_file2 = '100_seed_sample_vs_ideal.csv'


output_plot = 'impact_k_combine_CD'

# ===============================================================
# IDEAL VS STANDARD

df1 = pd.read_csv(input_file1, names=['sample','k','RBO','Jaccard','Cumulative_distance'])

num_sample = 16.62207358
#[5, 10, 15, 20, 100, 256]


kj15 = df1[(df1['k'] == 5) & (df1['sample'] == num_sample)]
kj15 = kj15['Cumulative_distance']

kj16 = df1[(df1['k'] == 10) & (df1['sample'] == num_sample)]
kj16 = kj16['Cumulative_distance']

kj17 = df1[(df1['k'] == 15) & (df1['sample'] == num_sample)]
kj17 = kj17['Cumulative_distance']

kj18 = df1[(df1['k'] == 20) & (df1['sample'] == num_sample)]
kj18 = kj18['Cumulative_distance']

kj19 = df1[(df1['k'] == 25) & (df1['sample'] == num_sample)]
kj19 = kj19['Cumulative_distance']

kj110 = df1[(df1['k'] == 25) & (df1['sample'] == num_sample)]
kj110 = kj110['Cumulative_distance']

kj111 = df1[(df1['k'] == 30) & (df1['sample'] == num_sample)]
kj111 = kj111['Cumulative_distance']

kj112 = df1[(df1['k'] == 35) & (df1['sample'] == num_sample)]
kj112 = kj112['Cumulative_distance']


kj113 = df1[(df1['k'] == 40) & (df1['sample'] == num_sample)]
kj113 = kj113['Cumulative_distance']

kj115 = df1[(df1['k'] == 45) & (df1['sample'] == num_sample)]
kj115 = kj115['Cumulative_distance']

kj120 = df1[(df1['k'] == 50) & (df1['sample'] == num_sample)]
kj120 = kj120['Cumulative_distance']




kj15 = list(mean_confidence_interval(kj15))
kj15.insert(0,5)
kj15.insert(1,'Cumulative_distance')

kj16 = list(mean_confidence_interval(kj16))
kj16.insert(0,10)
kj16.insert(1,'Cumulative_distance')

kj17 = list(mean_confidence_interval(kj17))
kj17.insert(0,15)
kj17.insert(1,'Cumulative_distance')

kj18 = list(mean_confidence_interval(kj18))
kj18.insert(0,20)
kj18.insert(1,'Cumulative_distance')

kj19 = list(mean_confidence_interval(kj19))
kj19.insert(0,25)
kj19.insert(1,'Cumulative_distance')

kj110 = list(mean_confidence_interval(kj110))
kj110.insert(0,30)
kj110.insert(1,'Cumulative_distance')

kj111 = list(mean_confidence_interval(kj111))
kj111.insert(0,35)
kj111.insert(1,'Cumulative_distance')

kj112 = list(mean_confidence_interval(kj112))
kj112.insert(0,40)
kj112.insert(1,'Cumulative_distance')

kj113 = list(mean_confidence_interval(kj113))
kj113.insert(0,45)
kj113.insert(1,'Cumulative_distance')

kj115 = list(mean_confidence_interval(kj115))
kj115.insert(0,50)
kj115.insert(1,'Cumulative_distance')

df1 = pd.DataFrame([kj15,kj16,kj17,kj18,kj19,kj110, kj111,kj112,kj113,kj115])
df1.columns = ['k','measurement','mean','lb','ub']



df2 = pd.read_csv(input_file2, names=['sample','k','RBO','Jaccard','Cumulative_distance'])

num_samp = 40
#[5, 10, 15, 20, 100, 256]


kjrow15 = df2[(df2['k'] == 5) & (df2['sample'] == num_samp)]
kjrow15 = kjrow15['Cumulative_distance']

kjrow16 = df2[(df2['k'] == 10) & (df2['sample'] == num_samp)]
kjrow16 = kjrow16['Cumulative_distance']

kjrow17 = df2[(df2['k'] == 15) & (df2['sample'] == num_samp)]
kjrow17 = kjrow17['Cumulative_distance']

kjrow18 = df2[(df2['k'] == 20) & (df2['sample'] == num_samp)]
kjrow18 = kjrow18['Cumulative_distance']

kjrow19 = df2[(df2['k'] == 25) & (df2['sample'] == num_samp)]
kjrow19 = kjrow19['Cumulative_distance']

kjrow110 = df2[(df2['k'] == 25) & (df2['sample'] == num_samp)]
kjrow110 = kjrow110['Cumulative_distance']

kjrow111 = df2[(df2['k'] == 30) & (df2['sample'] == num_samp)]
kjrow111 = kjrow111['Cumulative_distance']

kjrow112 = df2[(df2['k'] == 35) & (df2['sample'] == num_samp)]
kjrow112 = kjrow112['Cumulative_distance']


kjrow113 = df2[(df2['k'] == 40) & (df2['sample'] == num_samp)]
kjrow113 = kjrow113['Cumulative_distance']

kjrow115 = df2[(df2['k'] == 45) & (df2['sample'] == num_samp)]
kjrow115 = kjrow115['Cumulative_distance']

kjrow120 = df2[(df2['k'] == 50) & (df2['sample'] == num_samp)]
kjrow120 = kjrow120['Cumulative_distance']




kjrow15 = list(mean_confidence_interval(kjrow15))
kjrow15.insert(0,5)
kjrow15.insert(1,'Cumulative_distance')

kjrow16 = list(mean_confidence_interval(kjrow16))
kjrow16.insert(0,10)
kjrow16.insert(1,'Cumulative_distance')

kjrow17 = list(mean_confidence_interval(kjrow17))
kjrow17.insert(0,15)
kjrow17.insert(1,'Cumulative_distance')

kjrow18 = list(mean_confidence_interval(kjrow18))
kjrow18.insert(0,20)
kjrow18.insert(1,'Cumulative_distance')

kjrow19 = list(mean_confidence_interval(kjrow19))
kjrow19.insert(0,25)
kjrow19.insert(1,'Cumulative_distance')

kjrow110 = list(mean_confidence_interval(kjrow110))
kjrow110.insert(0,30)
kjrow110.insert(1,'Cumulative_distance')

kjrow111 = list(mean_confidence_interval(kjrow111))
kjrow111.insert(0,35)
kjrow111.insert(1,'Cumulative_distance')

kjrow112 = list(mean_confidence_interval(kjrow112))
kjrow112.insert(0,40)
kjrow112.insert(1,'Cumulative_distance')

kjrow113 = list(mean_confidence_interval(kjrow113))
kjrow113.insert(0,45)
kjrow113.insert(1,'Cumulative_distance')

kjrow115 = list(mean_confidence_interval(kjrow115))
kjrow115.insert(0,50)
kjrow115.insert(1,'Cumulative_distance')



df2 = pd.DataFrame([kjrow15,kjrow16,kjrow17,kjrow18,kjrow19,kjrow110, kjrow111,kjrow112,kjrow113,kjrow115])
df2.columns = ['k','measurement','mean','lb','ub']






mean1 = df1[df1['measurement'] == 'Cumulative_distance'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Cumulative_distance'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Cumulative_distance'].reset_index()
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
matplotlib.rc('figure', figsize = (14, 14))
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
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = 'RandomCellsImputed', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = 'SampleClean RowSC', marker='<', linestyle='-', linewidth=2, markersize=12)
# ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = 'CD', marker='o', linestyle='-', linewidth=2, markersize=12)
# ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'Similarity to reference', marker='s', linestyle='--', linewidth=2, markersize=12)
# ax.plot(mean5, lw = 1, color = '#0d0e0f', alpha = 1, label = 'Deviation/outstanding', marker='x', linestyle='-.', linewidth=2, markersize=12)


# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
# ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
# ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)
# ax.fill_between(t, lb5, ub5, color = '#87888a', alpha = 0.4)


# Label the axes and provide a title
ax.set_title("40 sample cleaned rows or 520 cleaned cells")
ax.set_xlabel("k")
ax.set_ylabel("Effectiveness, agF: AVG only")
x = [5,10,15,20,25,30,35,40,45,50]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.1)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()

