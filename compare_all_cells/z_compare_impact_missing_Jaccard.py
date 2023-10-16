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
# input_file4 = 'results/sim_missing_a_m_vs_ideal.csv'
# input_file5 = 'results/div_missing_a_m_vs_ideal.csv'


output_plot = 'Jaccard'

k = 10
# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file1, names=['sample','k','RBO','Jaccard','Cumulative_distance'])
df = df.dropna()

dfj110 = df[(df['k'] == k) & (df['sample'] == 19.96655518)]
dfj110 = dfj110['Jaccard']

dfj120 = df[(df['k'] == k) & (df['sample'] == 16.62207358)]
dfj120 = dfj120['Jaccard']

dfj130 = df[(df['k'] == k) & (df['sample'] == 13.27759197)]
dfj130 = dfj130['Jaccard']

dfj140 = df[(df['k'] == k) & (df['sample'] == 9.933110368)]
dfj140 = dfj140['Jaccard']

dfj150 = df[(df['k'] == k) & (df['sample'] == 6.5)]
dfj150 = dfj150['Jaccard']

dfj160 = df[(df['k'] == k) & (df['sample'] == 3.244147157)]
dfj160 = dfj160['Jaccard']

dfj170 = df[(df['k'] == k) & (df['sample'] == 0)]
dfj170 = dfj170['Jaccard']

dfj180 = df[(df['k'] == k) & (df['sample'] == 0)]
dfj180 = dfj180['Jaccard']

dfj190 = df[(df['k'] == k) & (df['sample'] == 0)]
dfj190 = dfj190['Jaccard']





dfj110 = list(mean_confidence_interval(dfj110))
dfj110.insert(0,19.96655518)
dfj110.insert(1,'Jaccard')

dfj120 = list(mean_confidence_interval(dfj120))
dfj120.insert(0,16.62207358)
dfj120.insert(1,'Jaccard')

dfj130 = list(mean_confidence_interval(dfj130))
dfj130.insert(0,13.27759197)
dfj130.insert(1,'Jaccard')

dfj140 = list(mean_confidence_interval(dfj140))
dfj140.insert(0,9.933110368)
dfj140.insert(1,'Jaccard')

dfj150 = list(mean_confidence_interval(dfj150))
dfj150.insert(0,6.5)
dfj150.insert(1,'Jaccard')

dfj160 = list(mean_confidence_interval(dfj160))
dfj160.insert(0,3.244147157)
dfj160.insert(1,'Jaccard')

dfj170 = list(mean_confidence_interval(dfj170))
dfj170.insert(0,0)
dfj170.insert(1,'Jaccard')

dfj180 = list(mean_confidence_interval(dfj180))
dfj180.insert(0,0)
dfj180.insert(1,'Jaccard')

dfj190 = list(mean_confidence_interval(dfj190))
dfj190.insert(0,0)
dfj190.insert(1,'Jaccard')



df = pd.read_csv(input_file2, names=['sample','k','RBO','Jaccard','Cumulative_distance'])


dfjrow110 = df[(df['k'] == k) & (df['sample'] == 100)]
dfjrow110 = dfjrow110['Jaccard']

dfjrow120 = df[(df['k'] == k) & (df['sample'] == 150)]
dfjrow120 = dfjrow120['Jaccard']

dfjrow130 = df[(df['k'] == k) & (df['sample'] == 30)]
dfjrow130 = dfjrow130['Jaccard']

dfjrow140 = df[(df['k'] == k) & (df['sample'] == 40)]
dfjrow140 = dfjrow140['Jaccard']

dfjrow150 = df[(df['k'] == k) & (df['sample'] == 50)]
dfjrow150 = dfjrow150['Jaccard']

dfjrow160 = df[(df['k'] == k) & (df['sample'] == 60)]
dfjrow160 = dfjrow160['Jaccard']

dfjrow170 = df[(df['k'] == k) & (df['sample'] == 70)]
dfjrow170 = dfjrow170['Jaccard']

dfjrow180 = df[(df['k'] == k) & (df['sample'] == 80)]
dfjrow180 = dfjrow180['Jaccard']

dfjrow190 = df[(df['k'] == k) & (df['sample'] == 90)]
dfjrow190 = dfjrow190['Jaccard']





dfjrow110 = list(mean_confidence_interval(dfjrow110))
dfjrow110.insert(0,100)
dfjrow110.insert(1,'Jaccard')

dfjrow120 = list(mean_confidence_interval(dfjrow120))
dfjrow120.insert(0,150)
dfjrow120.insert(1,'Jaccard')

dfjrow130 = list(mean_confidence_interval(dfjrow130))
dfjrow130.insert(0,30)
dfjrow130.insert(1,'Jaccard')

dfjrow140 = list(mean_confidence_interval(dfjrow140))
dfjrow140.insert(0,40)
dfjrow140.insert(1,'Jaccard')

dfjrow150 = list(mean_confidence_interval(dfjrow150))
dfjrow150.insert(0,50)
dfjrow150.insert(1,'Jaccard')

dfjrow160 = list(mean_confidence_interval(dfjrow160))
dfjrow160.insert(0,60)
dfjrow160.insert(1,'Jaccard')

dfjrow170 = list(mean_confidence_interval(dfjrow170))
dfjrow170.insert(0,70)
dfjrow170.insert(1,'Jaccard')

dfjrow180 = list(mean_confidence_interval(dfjrow180))
dfjrow180.insert(0,80)
dfjrow180.insert(1,'Jaccard')

dfjrow190 = list(mean_confidence_interval(dfjrow190))
dfjrow190.insert(0,90)
dfjrow190.insert(1,'Jaccard')




#print(dfj350)

df1 = pd.DataFrame([dfj110, dfj120, dfj130, dfj140, dfj150, dfj160, dfj170, dfj180, dfj190])
df1.columns = ['k','measurement','mean','lb','ub']
df2 = pd.DataFrame([dfjrow130, dfjrow140, dfjrow150, dfjrow160, dfjrow170, dfjrow180, dfjrow190, dfjrow110, dfjrow120])
df2.columns = ['k','measurement','mean','lb','ub']



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



# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (30, 14))
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
ax.set_title("Jaccard - 30 percent incomplete data, k = 10")
ax.set_xlabel("number of cleaned rows/cells")
ax.set_ylabel("Effectiveness: ag= only AVG")
x = ['30/390','40/520','50/650','60/780','70/910','80/1040','90/1170','100/1300','150/1950']
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()




















