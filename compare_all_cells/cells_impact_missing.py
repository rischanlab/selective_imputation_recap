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
input_file2 = '30_percent_missing.csv'
input_file3 = '30_percent_missing.csv'
# input_file4 = 'results/sim_missing_a_m_vs_ideal.csv'
# input_file5 = 'results/div_missing_a_m_vs_ideal.csv'


output_plot = '30_percent_missing'

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




dfj210 = df[(df['k'] == k) & (df['sample'] == 19.96655518)]
dfj210 = dfj210['RBO']

dfj220 = df[(df['k'] == k) & (df['sample'] == 16.62207358)]
dfj220 = dfj220['RBO']

dfj230 = df[(df['k'] == k) & (df['sample'] == 13.27759197)]
dfj230 = dfj230['RBO']

dfj240 = df[(df['k'] == k) & (df['sample'] == 9.933110368)]
dfj240 = dfj240['RBO']

dfj250 = df[(df['k'] == k) & (df['sample'] == 6.5)]
dfj250 = dfj250['RBO']

dfj260 = df[(df['k'] == k) & (df['sample'] == 3.244147157)]
dfj260 = dfj260['RBO']

dfj270 = df[(df['k'] == k) & (df['sample'] == 0)]
dfj270 = dfj270['RBO']

dfj280 = df[(df['k'] == k) & (df['sample'] == 0)]
dfj280 = dfj280['RBO']

dfj290 = df[(df['k'] == k) & (df['sample'] == 0)]
dfj290 = dfj290['RBO']





dfj210 = list(mean_confidence_interval(dfj210))
dfj210.insert(0,19.96655518)
dfj210.insert(1,'RBO')

dfj220 = list(mean_confidence_interval(dfj220))
dfj220.insert(0,16.62207358)
dfj220.insert(1,'RBO')

dfj230 = list(mean_confidence_interval(dfj230))
dfj230.insert(0,13.27759197)
dfj230.insert(1,'RBO')

dfj240 = list(mean_confidence_interval(dfj240))
dfj240.insert(0,9.933110368)
dfj240.insert(1,'RBO')

dfj250 = list(mean_confidence_interval(dfj250))
dfj250.insert(0,6.5)
dfj250.insert(1,'RBO')

dfj260 = list(mean_confidence_interval(dfj260))
dfj260.insert(0,3.244147157)
dfj260.insert(1,'RBO')

dfj270 = list(mean_confidence_interval(dfj270))
dfj270.insert(0,0)
dfj270.insert(1,'RBO')

dfj280 = list(mean_confidence_interval(dfj280))
dfj280.insert(0,0)
dfj280.insert(1,'RBO')

dfj290 = list(mean_confidence_interval(dfj290))
dfj290.insert(0,0)
dfj290.insert(1,'RBO')


df = pd.read_csv(input_file3, names=['sample','k','RBO','Jaccard','Cumulative_distance'])





dfj310 = df[(df['k'] == k) & (df['sample'] == 19.96655518)]
dfj310 = dfj310['Cumulative_distance']

dfj320 = df[(df['k'] == k) & (df['sample'] == 16.62207358)]
dfj320 = dfj320['Cumulative_distance']

dfj330 = df[(df['k'] == k) & (df['sample'] == 13.27759197)]
dfj330 = dfj330['Cumulative_distance']

dfj340 = df[(df['k'] == k) & (df['sample'] == 9.933110368)]
dfj340 = dfj340['Cumulative_distance']

dfj350 = df[(df['k'] == k) & (df['sample'] == 6.5)]
dfj350 = dfj350['Cumulative_distance']

dfj360 = df[(df['k'] == k) & (df['sample'] == 3.244147157)]
dfj360 = dfj360['Cumulative_distance']

dfj370 = df[(df['k'] == k) & (df['sample'] == 0)]
dfj370 = dfj370['Cumulative_distance']

dfj380 = df[(df['k'] == k) & (df['sample'] == 0)]
dfj380 = dfj380['Cumulative_distance']

dfj390 = df[(df['k'] == k) & (df['sample'] == 0)]
dfj390 = dfj390['Cumulative_distance']





dfj310 = list(mean_confidence_interval(dfj310))
dfj310.insert(0,19.96655518)
dfj310.insert(1,'Cumulative_distance')

dfj320 = list(mean_confidence_interval(dfj320))
dfj320.insert(0,16.62207358)
dfj320.insert(1,'Cumulative_distance')

dfj330 = list(mean_confidence_interval(dfj330))
dfj330.insert(0,13.27759197)
dfj330.insert(1,'Cumulative_distance')

dfj340 = list(mean_confidence_interval(dfj340))
dfj340.insert(0,9.933110368)
dfj340.insert(1,'Cumulative_distance')

dfj350 = list(mean_confidence_interval(dfj350))
dfj350.insert(0,6.5)
dfj350.insert(1,'Cumulative_distance')

dfj360 = list(mean_confidence_interval(dfj360))
dfj360.insert(0,3.244147157)
dfj360.insert(1,'Cumulative_distance')

dfj370 = list(mean_confidence_interval(dfj370))
dfj370.insert(0,0)
dfj370.insert(1,'Cumulative_distance')

dfj380 = list(mean_confidence_interval(dfj380))
dfj380.insert(0,0)
dfj380.insert(1,'Cumulative_distance')

dfj390 = list(mean_confidence_interval(dfj390))
dfj390.insert(0,0)
dfj390.insert(1,'Cumulative_distance')



#print(dfj350)

df1 = pd.DataFrame([dfj110, dfj120, dfj130, dfj140, dfj150, dfj160, dfj170, dfj180, dfj190])
df1.columns = ['k','measurement','mean','lb','ub']
df2 = pd.DataFrame([ dfj210, dfj220, dfj230, dfj240, dfj250, dfj260, dfj270, dfj280, dfj290])
df2.columns = ['k','measurement','mean','lb','ub']
df3 = pd.DataFrame([dfj310, dfj320, dfj330, dfj340, dfj350, dfj360, dfj370, dfj380, dfj390])
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
ax.set_title("Impact of sample number on Effectiveness, 95% CI, k = 10")
ax.set_xlabel("number of imputed cells")
ax.set_ylabel("Effectiveness: ag= only AVG")
x = [390, 520, 650, 780, 910, 1040, 1170, 1300, 1950]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.0)
ax.set_ylim(ymax=1.01)

ax.legend(loc='best')

plt.savefig('plot/' + output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('plot/' + output_plot + '.png')
plt.show()


