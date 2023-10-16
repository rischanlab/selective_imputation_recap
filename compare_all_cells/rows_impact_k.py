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

input_file1 = '100_seed_sample_vs_ideal.csv'
input_file2 = '100_seed_sample_vs_ideal.csv'
input_file3 = '100_seed_sample_vs_ideal.csv'

output_plot = 'impact_k'

# ===============================================================
# IDEAL VS STANDARD

df1 = pd.read_csv(input_file1, names=['sample','k','RBO','Jaccard','Cumulative_distance'])

num_sample = 100
#[5, 10, 15, 20, 100, 256]


kj15 = df1[(df1['k'] == 5) & (df1['sample'] == num_sample)]
kj15 = kj15['Jaccard']

kj16 = df1[(df1['k'] == 10) & (df1['sample'] == num_sample)]
kj16 = kj16['Jaccard']

kj17 = df1[(df1['k'] == 15) & (df1['sample'] == num_sample)]
kj17 = kj17['Jaccard']

kj18 = df1[(df1['k'] == 20) & (df1['sample'] == num_sample)]
kj18 = kj18['Jaccard']

kj19 = df1[(df1['k'] == 25) & (df1['sample'] == num_sample)]
kj19 = kj19['Jaccard']

kj110 = df1[(df1['k'] == 25) & (df1['sample'] == num_sample)]
kj110 = kj110['Jaccard']

kj111 = df1[(df1['k'] == 30) & (df1['sample'] == num_sample)]
kj111 = kj111['Jaccard']

kj112 = df1[(df1['k'] == 35) & (df1['sample'] == num_sample)]
kj112 = kj112['Jaccard']


kj113 = df1[(df1['k'] == 40) & (df1['sample'] == num_sample)]
kj113 = kj113['Jaccard']

kj115 = df1[(df1['k'] == 45) & (df1['sample'] == num_sample)]
kj115 = kj115['Jaccard']

kj120 = df1[(df1['k'] == 50) & (df1['sample'] == num_sample)]
kj120 = kj120['Jaccard']




kj15 = list(mean_confidence_interval(kj15))
kj15.insert(0,5)
kj15.insert(1,'Jaccard')

kj16 = list(mean_confidence_interval(kj16))
kj16.insert(0,10)
kj16.insert(1,'Jaccard')

kj17 = list(mean_confidence_interval(kj17))
kj17.insert(0,15)
kj17.insert(1,'Jaccard')

kj18 = list(mean_confidence_interval(kj18))
kj18.insert(0,20)
kj18.insert(1,'Jaccard')

kj19 = list(mean_confidence_interval(kj19))
kj19.insert(0,25)
kj19.insert(1,'Jaccard')

kj110 = list(mean_confidence_interval(kj110))
kj110.insert(0,30)
kj110.insert(1,'Jaccard')

kj111 = list(mean_confidence_interval(kj111))
kj111.insert(0,35)
kj111.insert(1,'Jaccard')

kj112 = list(mean_confidence_interval(kj112))
kj112.insert(0,40)
kj112.insert(1,'Jaccard')

kj113 = list(mean_confidence_interval(kj113))
kj113.insert(0,45)
kj113.insert(1,'Jaccard')

kj115 = list(mean_confidence_interval(kj115))
kj115.insert(0,50)
kj115.insert(1,'Jaccard')

df1 = pd.DataFrame([kj15,kj16,kj17,kj18,kj19,kj110, kj111,kj112,kj113,kj115])
df1.columns = ['k','measurement','mean','lb','ub']


df2 = pd.read_csv(input_file2, names=['sample','k','RBO','Jaccard','Cumulative_distance'])




kr15 = df2[(df2['k'] == 5) & (df2['sample'] == num_sample)]
kr15 = kr15['RBO']

kr16 = df2[(df2['k'] == 10) & (df2['sample'] == num_sample)]
kr16 = kr16['RBO']

kr17 = df2[(df2['k'] == 15) & (df2['sample'] == num_sample)]
kr17 = kr17['RBO']

kr18 = df2[(df2['k'] == 20) & (df2['sample'] == num_sample)]
kr18 = kr18['RBO']

kr19 = df2[(df2['k'] == 25) & (df2['sample'] == num_sample)]
kr19 = kr19['RBO']

kr110 = df2[(df2['k'] == 25) & (df2['sample'] == num_sample)]
kr110 = kr110['RBO']

kr111 = df2[(df2['k'] == 30) & (df2['sample'] == num_sample)]
kr111 = kr111['RBO']

kr112 = df2[(df2['k'] == 35) & (df2['sample'] == num_sample)]
kr112 = kr112['RBO']


kr113 = df2[(df2['k'] == 40) & (df2['sample'] == num_sample)]
kr113 = kr113['RBO']

kr115 = df2[(df2['k'] == 45) & (df2['sample'] == num_sample)]
kr115 = kr115['RBO']

kr120 = df2[(df2['k'] == 50) & (df2['sample'] == num_sample)]
kr120 = kr120['RBO']




kr15 = list(mean_confidence_interval(kr15))
kr15.insert(0,5)
kr15.insert(1,'RBO')

kr16 = list(mean_confidence_interval(kr16))
kr16.insert(0,10)
kr16.insert(1,'RBO')

kr17 = list(mean_confidence_interval(kr17))
kr17.insert(0,15)
kr17.insert(1,'RBO')

kr18 = list(mean_confidence_interval(kr18))
kr18.insert(0,20)
kr18.insert(1,'RBO')

kr19 = list(mean_confidence_interval(kr19))
kr19.insert(0,25)
kr19.insert(1,'RBO')

kr110 = list(mean_confidence_interval(kr110))
kr110.insert(0,30)
kr110.insert(1,'RBO')

kr111 = list(mean_confidence_interval(kr111))
kr111.insert(0,35)
kr111.insert(1,'RBO')

kr112 = list(mean_confidence_interval(kr112))
kr112.insert(0,40)
kr112.insert(1,'RBO')

kr113 = list(mean_confidence_interval(kr113))
kr113.insert(0,45)
kr113.insert(1,'RBO')

kr115 = list(mean_confidence_interval(kr115))
kr115.insert(0,50)
kr115.insert(1,'RBO')

df2 = pd.DataFrame([kr15,kr16,kr17,kr18,kr19,kr110, kr111,kr112,kr113,kr115])
df2.columns = ['k','measurement','mean','lb','ub']



df3 = pd.read_csv(input_file3, names=['sample','k','RBO','Jaccard','Cumulative_distance'])




kc15 = df3[(df3['k'] == 5) & (df3['sample'] == num_sample)]
kc15 = kc15['Cumulative_distance']

kc16 = df3[(df3['k'] == 10) & (df3['sample'] == num_sample)]
kc16 = kc16['Cumulative_distance']

kc17 = df3[(df3['k'] == 15) & (df3['sample'] == num_sample)]
kc17 = kc17['Cumulative_distance']

kc18 = df3[(df3['k'] == 20) & (df3['sample'] == num_sample)]
kc18 = kc18['Cumulative_distance']

kc19 = df3[(df3['k'] == 25) & (df3['sample'] == num_sample)]
kc19 = kc19['Cumulative_distance']

kc110 = df3[(df3['k'] == 25) & (df3['sample'] == num_sample)]
kc110 = kc110['Cumulative_distance']

kc111 = df3[(df3['k'] == 30) & (df3['sample'] == num_sample)]
kc111 = kc111['Cumulative_distance']

kc112 = df3[(df3['k'] == 35) & (df3['sample'] == num_sample)]
kc112 = kc112['Cumulative_distance']


kc113 = df3[(df3['k'] == 40) & (df3['sample'] == num_sample)]
kc113 = kc113['Cumulative_distance']

kc115 = df3[(df3['k'] == 45) & (df3['sample'] == num_sample)]
kc115 = kc115['Cumulative_distance']

kc120 = df3[(df3['k'] == 50) & (df3['sample'] == num_sample)]
kc120 = kc120['Cumulative_distance']




kc15 = list(mean_confidence_interval(kc15))
kc15.insert(0,5)
kc15.insert(1,'Cumulative_distance')

kc16 = list(mean_confidence_interval(kc16))
kc16.insert(0,10)
kc16.insert(1,'Cumulative_distance')

kc17 = list(mean_confidence_interval(kc17))
kc17.insert(0,15)
kc17.insert(1,'Cumulative_distance')

kc18 = list(mean_confidence_interval(kc18))
kc18.insert(0,20)
kc18.insert(1,'Cumulative_distance')

kc19 = list(mean_confidence_interval(kc19))
kc19.insert(0,25)
kc19.insert(1,'Cumulative_distance')

kc110 = list(mean_confidence_interval(kc110))
kc110.insert(0,30)
kc110.insert(1,'Cumulative_distance')

kc111 = list(mean_confidence_interval(kc111))
kc111.insert(0,35)
kc111.insert(1,'Cumulative_distance')

kc112 = list(mean_confidence_interval(kc112))
kc112.insert(0,40)
kc112.insert(1,'Cumulative_distance')

kc113 = list(mean_confidence_interval(kc113))
kc113.insert(0,45)
kc113.insert(1,'Cumulative_distance')

kc115 = list(mean_confidence_interval(kc115))
kc115.insert(0,50)
kc115.insert(1,'Cumulative_distance')

df3 = pd.DataFrame([kc15,kc16,kc17,kc18,kc19,kc110, kc111,kc112,kc113,kc115])
df3.columns = ['k','measurement','mean','lb','ub']




mean1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb1 = lb1['lb']

mean2 = df2[df2['measurement'] == 'RBO'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'RBO'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'RBO'].reset_index()
lb2 = lb2['lb']

mean3 = df3[df3['measurement'] == 'Cumulative_distance'].reset_index()
mean3 = mean3['mean']
ub3 = df3[df3['measurement'] == 'Cumulative_distance'].reset_index()
ub3 = ub3['ub']
lb3 = df3[df3['measurement'] == 'Cumulative_distance'].reset_index()
lb3 = lb3['lb']

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
ax.plot(mean1, lw = 1, color = '#539caf', alpha = 1, label = 'Jaccard', marker='x', linestyle='-.', linewidth=2, markersize=12)
ax.plot(mean2, lw = 1, color = '#b65332', alpha = 1, label = 'RBO', marker='<', linestyle='-', linewidth=2, markersize=12)
ax.plot(mean3, lw = 1, color = '#5be19a', alpha = 1, label = 'CD', marker='o', linestyle='-', linewidth=2, markersize=12)
# ax.plot(mean4, lw = 1, color = '#ece554', alpha = 1, label = 'Similarity to reference', marker='s', linestyle='--', linewidth=2, markersize=12)
# ax.plot(mean5, lw = 1, color = '#0d0e0f', alpha = 1, label = 'Deviation/outstanding', marker='x', linestyle='-.', linewidth=2, markersize=12)


# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#539caf', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#b65332', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#5be19a', alpha = 0.4)
# ax.fill_between(t, lb4, ub4, color = '#ffff80', alpha = 0.4)
# ax.fill_between(t, lb5, ub5, color = '#87888a', alpha = 0.4)


# Label the axes and provide a title
ax.set_title("Impact of k on Effectiveness, 95% CI, 100 num samples (rows)")
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

