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

input_file1 = '30_percent_missing_correct.csv'
input_file2 = '100_seed_sample_vs_ideal.csv'
# input_file4 = 'results/sim_missing_a_m_vs_ideal.csv'
# input_file5 = 'results/div_missing_a_m_vs_ideal.csv'


output_plot = 'CD'

k = 10
# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file1, names=['sample','k','RBO','Jaccard','Cumulative_distance'])
df = df.dropna()

dfj110 = df[(df['k'] == k) & (df['sample'] == 26.98996656)]
dfj110 = dfj110['Cumulative_distance']

dfj120 = df[(df['k'] == k) & (df['sample'] == 25.98662207)]
dfj120 = dfj120['Cumulative_distance']

dfj130 = df[(df['k'] == k) & (df['sample'] == 24.98327759)]
dfj130 = dfj130['Cumulative_distance']

dfj140 = df[(df['k'] == k) & (df['sample'] == 23.97993311)]
dfj140 = dfj140['Cumulative_distance']

dfj150 = df[(df['k'] == k) & (df['sample'] == 22.97658863)]
dfj150 = dfj150['Cumulative_distance']

dfj160 = df[(df['k'] == k) & (df['sample'] == 21.97324415)]
dfj160 = dfj160['Cumulative_distance']

dfj170 = df[(df['k'] == k) & (df['sample'] == 20.96989967)]
dfj170 = dfj170['Cumulative_distance']

dfj180 = df[(df['k'] == k) & (df['sample'] == 19.96655518)]
dfj180 = dfj180['Cumulative_distance']

dfj190 = df[(df['k'] == k) & (df['sample'] == 14.94983278)]
dfj190 = dfj190['Cumulative_distance']


dfj200 = df[(df['k'] == k) & (df['sample'] == 9.933110368)]
dfj200 = dfj200['Cumulative_distance']

dfj210 = df[(df['k'] == k) & (df['sample'] == 4.91638796)]
dfj210 = dfj210['Cumulative_distance']

dfj220 = df[(df['k'] == k) & (df['sample'] == 0)]
dfj220 = dfj220['Cumulative_distance']


dfj110 = list(mean_confidence_interval(dfj110))
dfj110.insert(0,26.98996656)
dfj110.insert(1,'Cumulative_distance')

dfj120 = list(mean_confidence_interval(dfj120))
dfj120.insert(0,25.98662207)
dfj120.insert(1,'Cumulative_distance')

dfj130 = list(mean_confidence_interval(dfj130))
dfj130.insert(0,24.98327759)
dfj130.insert(1,'Cumulative_distance')

dfj140 = list(mean_confidence_interval(dfj140))
dfj140.insert(0,23.97993311)
dfj140.insert(1,'Cumulative_distance')

dfj150 = list(mean_confidence_interval(dfj150))
dfj150.insert(0,22.97658863)
dfj150.insert(1,'Cumulative_distance')

dfj160 = list(mean_confidence_interval(dfj160))
dfj160.insert(0,21.97324415)
dfj160.insert(1,'Cumulative_distance')

dfj170 = list(mean_confidence_interval(dfj170))
dfj170.insert(0,20.96989967)
dfj170.insert(1,'Cumulative_distance')

dfj180 = list(mean_confidence_interval(dfj180))
dfj180.insert(0,19.96655518)
dfj180.insert(1,'Cumulative_distance')

dfj190 = list(mean_confidence_interval(dfj190))
dfj190.insert(0,14.94983278)
dfj190.insert(1,'Cumulative_distance')


dfj200 = list(mean_confidence_interval(dfj200))
dfj200.insert(0,9.933110368)
dfj200.insert(1,'Cumulative_distance')

dfj210 = list(mean_confidence_interval(dfj210))
dfj210.insert(0,4.91638796)
dfj210.insert(1,'Cumulative_distance')

dfj220 = list(mean_confidence_interval(dfj220))
dfj220.insert(0,0)
dfj220.insert(1,'Cumulative_distance')


df = pd.read_csv(input_file2, names=['sample','k','RBO','Jaccard','Cumulative_distance'])


dfjrow110 = df[(df['k'] == k) & (df['sample'] == 100)]
dfjrow110 = dfjrow110['Cumulative_distance']

dfjrow120 = df[(df['k'] == k) & (df['sample'] == 150)]
dfjrow120 = dfjrow120['Cumulative_distance']

dfjrow130 = df[(df['k'] == k) & (df['sample'] == 30)]
dfjrow130 = dfjrow130['Cumulative_distance']

dfjrow140 = df[(df['k'] == k) & (df['sample'] == 40)]
dfjrow140 = dfjrow140['Cumulative_distance']

dfjrow150 = df[(df['k'] == k) & (df['sample'] == 50)]
dfjrow150 = dfjrow150['Cumulative_distance']

dfjrow160 = df[(df['k'] == k) & (df['sample'] == 60)]
dfjrow160 = dfjrow160['Cumulative_distance']

dfjrow170 = df[(df['k'] == k) & (df['sample'] == 70)]
dfjrow170 = dfjrow170['Cumulative_distance']

dfjrow180 = df[(df['k'] == k) & (df['sample'] == 80)]
dfjrow180 = dfjrow180['Cumulative_distance']

dfjrow190 = df[(df['k'] == k) & (df['sample'] == 90)]
dfjrow190 = dfjrow190['Cumulative_distance']


dfjrow200 = df[(df['k'] == k) & (df['sample'] == 200)]
dfjrow200 = dfjrow200['Cumulative_distance']

dfjrow250 = df[(df['k'] == k) & (df['sample'] == 250)]
dfjrow250 = dfjrow250['Cumulative_distance']

dfjrow299 = df[(df['k'] == k) & (df['sample'] == 299)]
dfjrow299 = dfjrow299['Cumulative_distance']




dfjrow110 = list(mean_confidence_interval(dfjrow110))
dfjrow110.insert(0,100)
dfjrow110.insert(1,'Cumulative_distance')

dfjrow120 = list(mean_confidence_interval(dfjrow120))
dfjrow120.insert(0,150)
dfjrow120.insert(1,'Cumulative_distance')

dfjrow130 = list(mean_confidence_interval(dfjrow130))
dfjrow130.insert(0,30)
dfjrow130.insert(1,'Cumulative_distance')

dfjrow140 = list(mean_confidence_interval(dfjrow140))
dfjrow140.insert(0,40)
dfjrow140.insert(1,'Cumulative_distance')

dfjrow150 = list(mean_confidence_interval(dfjrow150))
dfjrow150.insert(0,50)
dfjrow150.insert(1,'Cumulative_distance')

dfjrow160 = list(mean_confidence_interval(dfjrow160))
dfjrow160.insert(0,60)
dfjrow160.insert(1,'Cumulative_distance')

dfjrow170 = list(mean_confidence_interval(dfjrow170))
dfjrow170.insert(0,70)
dfjrow170.insert(1,'Cumulative_distance')

dfjrow180 = list(mean_confidence_interval(dfjrow180))
dfjrow180.insert(0,80)
dfjrow180.insert(1,'Cumulative_distance')

dfjrow190 = list(mean_confidence_interval(dfjrow190))
dfjrow190.insert(0,90)
dfjrow190.insert(1,'Cumulative_distance')


dfjrow200 = list(mean_confidence_interval(dfjrow200))
dfjrow200.insert(0,200)
dfjrow200.insert(1,'Cumulative_distance')

dfjrow250 = list(mean_confidence_interval(dfjrow250))
dfjrow250.insert(0,250)
dfjrow250.insert(1,'Cumulative_distance')

dfjrow299 = list(mean_confidence_interval(dfjrow299))
dfjrow299.insert(0,299)
dfjrow299.insert(1,'Cumulative_distance')



#print(dfj350)

df1 = pd.DataFrame([dfj110, dfj120, dfj130, dfj140, dfj150, dfj160, dfj170, dfj180, dfj190, dfj200, dfj210, dfj220])
df1.columns = ['k','measurement','mean','lb','ub']
df2 = pd.DataFrame([dfjrow130, dfjrow140, dfjrow150, dfjrow160, dfjrow170, dfjrow180, dfjrow190, dfjrow110, dfjrow120, dfjrow200, dfjrow250, dfjrow299])
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
matplotlib.rc('figure', figsize = (40, 14))
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
ax.set_title("CD - 30 percent incomplete data, k = 10")
ax.set_xlabel("number of cleaned rows/missing values imputed")
ax.set_ylabel("Effectiveness: ag= only AVG")
x = ['30/117',
'40/156',
'50/195',
'60/234',
'70/273',
'80/312',
'90/351',
'100/390',
'150/585',
'200/780',
'250/975',
'299/1167']
xi = list(range(len(x)))
plt.xticks(xi, x, fontsize=18)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()




















