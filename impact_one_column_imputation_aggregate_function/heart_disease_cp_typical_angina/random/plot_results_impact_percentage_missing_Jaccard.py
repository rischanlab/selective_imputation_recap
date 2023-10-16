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

input_file1 = 'results/avg_ideal_rand_impute.csv'
# input_file2 = 'results/sum_missing_vs_ideal.csv'
# input_file3 = 'results/sumavg_missing_vs_ideal.csv'
input_file4 = 'results/max_ideal_rand_impute.csv'
# input_file5 = 'results/suicides100kpop_impute.csv'
# input_file6 = 'results/suicidesno_impute.csv'
# input_file7 = 'results/missing_vs_ideal.csv'




output_plot = 'jaccard_impact_incomplete_data'

k = 25
# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file1, names=['percentage','k','RBO','Jaccard','Cumulative_distance'])

dfj100 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj100 = dfj100['Jaccard']

dfj110 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfj110 = dfj110['Jaccard']

dfj120 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj120 = dfj120['Jaccard']

dfj130 = df[(df['k'] == k) & (df['percentage'] == 15)]
dfj130 = dfj130['Jaccard']

dfj140 = df[(df['k'] == k) & (df['percentage'] == 20)]
dfj140 = dfj140['Jaccard']

# dfj150 = df[(df['k'] == k) & (df['percentage'] == 50)]
# dfj150 = dfj150['Jaccard']

# dfj160 = df[(df['k'] == k) & (df['percentage'] == 60)]
# dfj160 = dfj160['Jaccard']

# dfj170 = df[(df['k'] == k) & (df['percentage'] == 70)]
# dfj170 = dfj170['Jaccard']





dfj100 = list(mean_confidence_interval(dfj100))
dfj100.insert(0,0)
dfj100.insert(1,'Jaccard')

dfj110 = list(mean_confidence_interval(dfj110))
dfj110.insert(0,5)
dfj110.insert(1,'Jaccard')

dfj120 = list(mean_confidence_interval(dfj120))
dfj120.insert(0,10)
dfj120.insert(1,'Jaccard')

dfj130 = list(mean_confidence_interval(dfj130))
dfj130.insert(0,15)
dfj130.insert(1,'Jaccard')

dfj140 = list(mean_confidence_interval(dfj140))
dfj140.insert(0,20)
dfj140.insert(1,'Jaccard')

# dfj150 = list(mean_confidence_interval(dfj150))
# dfj150.insert(0,50)
# dfj150.insert(1,'Jaccard')

# dfj160 = list(mean_confidence_interval(dfj160))
# dfj160.insert(0,60)
# dfj160.insert(1,'Jaccard')

# dfj170 = list(mean_confidence_interval(dfj170))
# dfj170.insert(0,70)
# dfj170.insert(1,'Jaccard')





# df = pd.read_csv(input_file2, names=['percentage','k','RBO','Jaccard','Cumulative_distance'])


# dfj200 = df[(df['k'] == k) & (df['percentage'] == 0)]
# dfj200 = dfj200['Jaccard']

# dfj210 = df[(df['k'] == k) & (df['percentage'] == 10)]
# dfj210 = dfj210['Jaccard']

# dfj220 = df[(df['k'] == k) & (df['percentage'] == 20)]
# dfj220 = dfj220['Jaccard']

# dfj230 = df[(df['k'] == k) & (df['percentage'] == 30)]
# dfj230 = dfj230['Jaccard']

# dfj240 = df[(df['k'] == k) & (df['percentage'] == 40)]
# dfj240 = dfj240['Jaccard']

# # dfj250 = df[(df['k'] == k) & (df['percentage'] == 50)]
# # dfj250 = dfj250['Jaccard']

# # dfj260 = df[(df['k'] == k) & (df['percentage'] == 60)]
# # dfj260 = dfj260['Jaccard']

# # dfj270 = df[(df['k'] == k) & (df['percentage'] == 70)]
# # dfj270 = dfj270['Jaccard']



# dfj200 = list(mean_confidence_interval(dfj200))
# dfj200.insert(0,0)
# dfj200.insert(1,'Jaccard')

# dfj210 = list(mean_confidence_interval(dfj210))
# dfj210.insert(0,10)
# dfj210.insert(1,'Jaccard')

# dfj220 = list(mean_confidence_interval(dfj220))
# dfj220.insert(0,20)
# dfj220.insert(1,'Jaccard')

# dfj230 = list(mean_confidence_interval(dfj230))
# dfj230.insert(0,30)
# dfj230.insert(1,'Jaccard')

# dfj240 = list(mean_confidence_interval(dfj240))
# dfj240.insert(0,40)
# dfj240.insert(1,'Jaccard')

# # dfj250 = list(mean_confidence_interval(dfj250))
# # dfj250.insert(0,50)
# # dfj250.insert(1,'Jaccard')

# # dfj260 = list(mean_confidence_interval(dfj260))
# # dfj260.insert(0,60)
# # dfj260.insert(1,'Jaccard')

# # dfj270 = list(mean_confidence_interval(dfj270))
# # dfj270.insert(0,70)
# # dfj270.insert(1,'Jaccard')




# df = pd.read_csv(input_file3, names=['percentage','k','RBO','Jaccard','Cumulative_distance'])



# dfj300 = df[(df['k'] == k) & (df['percentage'] == 0)]
# dfj300 = dfj300['Jaccard']

# dfj310 = df[(df['k'] == k) & (df['percentage'] == 10)]
# dfj310 = dfj310['Jaccard']

# dfj320 = df[(df['k'] == k) & (df['percentage'] == 20)]
# dfj320 = dfj320['Jaccard']

# dfj330 = df[(df['k'] == k) & (df['percentage'] == 30)]
# dfj330 = dfj330['Jaccard']

# dfj340 = df[(df['k'] == k) & (df['percentage'] == 40)]
# dfj340 = dfj340['Jaccard']

# # dfj350 = df[(df['k'] == k) & (df['percentage'] == 50)]
# # dfj350 = dfj350['Jaccard']

# # dfj360 = df[(df['k'] == k) & (df['percentage'] == 60)]
# # dfj360 = dfj360['Jaccard']

# # dfj370 = df[(df['k'] == k) & (df['percentage'] == 70)]
# # dfj370 = dfj370['Jaccard']



# dfj300 = list(mean_confidence_interval(dfj300))
# dfj300.insert(0,0)
# dfj300.insert(1,'Jaccard')

# dfj310 = list(mean_confidence_interval(dfj310))
# dfj310.insert(0,10)
# dfj310.insert(1,'Jaccard')

# dfj320 = list(mean_confidence_interval(dfj320))
# dfj320.insert(0,20)
# dfj320.insert(1,'Jaccard')

# dfj330 = list(mean_confidence_interval(dfj330))
# dfj330.insert(0,30)
# dfj330.insert(1,'Jaccard')

# dfj340 = list(mean_confidence_interval(dfj340))
# dfj340.insert(0,40)
# dfj340.insert(1,'Jaccard')

# dfj350 = list(mean_confidence_interval(dfj350))
# dfj350.insert(0,50)
# dfj350.insert(1,'Jaccard')

# dfj360 = list(mean_confidence_interval(dfj360))
# dfj360.insert(0,60)
# dfj360.insert(1,'Jaccard')

# dfj370 = list(mean_confidence_interval(dfj370))
# dfj370.insert(0,70)
# dfj370.insert(1,'Jaccard')





df = pd.read_csv(input_file4, names=['percentage','k','RBO','Jaccard','Cumulative_distance'])



dfj400 = df[(df['k'] == k) & (df['percentage'] == 0)]
dfj400 = dfj400['Jaccard']

dfj410 = df[(df['k'] == k) & (df['percentage'] == 5)]
dfj410 = dfj410['Jaccard']

dfj420 = df[(df['k'] == k) & (df['percentage'] == 10)]
dfj420 = dfj420['Jaccard']

dfj430 = df[(df['k'] == k) & (df['percentage'] == 15)]
dfj430 = dfj430['Jaccard']

dfj440 = df[(df['k'] == k) & (df['percentage'] == 20)]
dfj440 = dfj440['Jaccard']

# dfj450 = df[(df['k'] == k) & (df['percentage'] == 50)]
# dfj450 = dfj450['Jaccard']

# dfj460 = df[(df['k'] == k) & (df['percentage'] == 60)]
# dfj460 = dfj460['Jaccard']

# dfj470 = df[(df['k'] == k) & (df['percentage'] == 70)]
# dfj470 = dfj470['Jaccard']




dfj400 = list(mean_confidence_interval(dfj400))
dfj400.insert(0,0)
dfj400.insert(1,'Jaccard')

dfj410 = list(mean_confidence_interval(dfj410))
dfj410.insert(0,5)
dfj410.insert(1,'Jaccard')

dfj420 = list(mean_confidence_interval(dfj420))
dfj420.insert(0,10)
dfj420.insert(1,'Jaccard')

dfj430 = list(mean_confidence_interval(dfj430))
dfj430.insert(0,15)
dfj430.insert(1,'Jaccard')

dfj440 = list(mean_confidence_interval(dfj440))
dfj440.insert(0,20)
dfj440.insert(1,'Jaccard')

# dfj450 = list(mean_confidence_interval(dfj450))
# dfj450.insert(0,50)
# dfj450.insert(1,'Jaccard')

# dfj460 = list(mean_confidence_interval(dfj460))
# dfj460.insert(0,60)
# dfj460.insert(1,'Jaccard')

# dfj470 = list(mean_confidence_interval(dfj470))
# dfj470.insert(0,70)
# dfj470.insert(1,'Jaccard')




# df = pd.read_csv(input_file5, names=['percentage','k','RBO','Jaccard','Cumulative_distance'])


# dfj500 = df[(df['k'] == k) & (df['percentage'] == 0)]
# dfj500 = dfj500['Jaccard']

# dfj510 = df[(df['k'] == k) & (df['percentage'] == 10)]
# dfj510 = dfj510['Jaccard']

# dfj520 = df[(df['k'] == k) & (df['percentage'] == 20)]
# dfj520 = dfj520['Jaccard']

# dfj530 = df[(df['k'] == k) & (df['percentage'] == 30)]
# dfj530 = dfj530['Jaccard']

# dfj540 = df[(df['k'] == k) & (df['percentage'] == 40)]
# dfj540 = dfj540['Jaccard']

# dfj550 = df[(df['k'] == k) & (df['percentage'] == 50)]
# dfj550 = dfj550['Jaccard']

# dfj560 = df[(df['k'] == k) & (df['percentage'] == 60)]
# dfj560 = dfj560['Jaccard']

# dfj570 = df[(df['k'] == k) & (df['percentage'] == 70)]
# dfj570 = dfj570['Jaccard']



# dfj500 = list(mean_confidence_interval(dfj500))
# dfj500.insert(0,0)
# dfj500.insert(1,'Jaccard')

# dfj510 = list(mean_confidence_interval(dfj510))
# dfj510.insert(0,10)
# dfj510.insert(1,'Jaccard')

# dfj520 = list(mean_confidence_interval(dfj520))
# dfj520.insert(0,20)
# dfj520.insert(1,'Jaccard')

# dfj530 = list(mean_confidence_interval(dfj530))
# dfj530.insert(0,30)
# dfj530.insert(1,'Jaccard')

# dfj540 = list(mean_confidence_interval(dfj540))
# dfj540.insert(0,40)
# dfj540.insert(1,'Jaccard')

# dfj550 = list(mean_confidence_interval(dfj550))
# dfj550.insert(0,50)
# dfj550.insert(1,'Jaccard')

# dfj560 = list(mean_confidence_interval(dfj560))
# dfj560.insert(0,60)
# dfj560.insert(1,'Jaccard')

# dfj570 = list(mean_confidence_interval(dfj570))
# dfj570.insert(0,70)
# dfj570.insert(1,'Jaccard')



# df = pd.read_csv(input_file6, names=['percentage','k','RBO','Jaccard','Cumulative_distance'])


# dfj600 = df[(df['k'] == k) & (df['percentage'] == 0)]
# dfj600 = dfj600['Jaccard']

# dfj610 = df[(df['k'] == k) & (df['percentage'] == 10)]
# dfj610 = dfj610['Jaccard']

# dfj620 = df[(df['k'] == k) & (df['percentage'] == 20)]
# dfj620 = dfj620['Jaccard']

# dfj630 = df[(df['k'] == k) & (df['percentage'] == 30)]
# dfj630 = dfj630['Jaccard']

# dfj640 = df[(df['k'] == k) & (df['percentage'] == 40)]
# dfj640 = dfj640['Jaccard']

# dfj650 = df[(df['k'] == k) & (df['percentage'] == 50)]
# dfj650 = dfj650['Jaccard']

# dfj660 = df[(df['k'] == k) & (df['percentage'] == 60)]
# dfj660 = dfj660['Jaccard']

# dfj670 = df[(df['k'] == k) & (df['percentage'] == 70)]
# dfj670 = dfj670['Jaccard']

# dfj600 = list(mean_confidence_interval(dfj600))
# dfj600.insert(0,0)
# dfj600.insert(1,'Jaccard')

# dfj610 = list(mean_confidence_interval(dfj610))
# dfj610.insert(0,10)
# dfj610.insert(1,'Jaccard')

# dfj620 = list(mean_confidence_interval(dfj620))
# dfj620.insert(0,20)
# dfj620.insert(1,'Jaccard')

# dfj630 = list(mean_confidence_interval(dfj630))
# dfj630.insert(0,30)
# dfj630.insert(1,'Jaccard')

# dfj640 = list(mean_confidence_interval(dfj640))
# dfj640.insert(0,40)
# dfj640.insert(1,'Jaccard')

# dfj650 = list(mean_confidence_interval(dfj650))
# dfj650.insert(0,50)
# dfj650.insert(1,'Jaccard')

# dfj660 = list(mean_confidence_interval(dfj660))
# dfj660.insert(0,60)
# dfj660.insert(1,'Jaccard')

# dfj670 = list(mean_confidence_interval(dfj670))
# dfj670.insert(0,70)
# dfj670.insert(1,'Jaccard')


# df = pd.read_csv(input_file7, names=['percentage','k','RBO','Jaccard','Cumulative_distance'])


# dfj700 = df[(df['k'] == k) & (df['percentage'] == 0)]
# dfj700 = dfj700['Jaccard']

# dfj710 = df[(df['k'] == k) & (df['percentage'] == 10)]
# dfj710 = dfj710['Jaccard']

# dfj720 = df[(df['k'] == k) & (df['percentage'] == 20)]
# dfj720 = dfj720['Jaccard']

# dfj730 = df[(df['k'] == k) & (df['percentage'] == 30)]
# dfj730 = dfj730['Jaccard']

# dfj740 = df[(df['k'] == k) & (df['percentage'] == 40)]
# dfj740 = dfj740['Jaccard']

# dfj750 = df[(df['k'] == k) & (df['percentage'] == 50)]
# dfj750 = dfj750['Jaccard']

# dfj760 = df[(df['k'] == k) & (df['percentage'] == 60)]
# dfj760 = dfj760['Jaccard']

# dfj770 = df[(df['k'] == k) & (df['percentage'] == 70)]
# dfj770 = dfj770['Jaccard']




# dfj700 = list(mean_confidence_interval(dfj700))
# dfj700.insert(0,0)
# dfj700.insert(1,'Jaccard')

# dfj710 = list(mean_confidence_interval(dfj710))
# dfj710.insert(0,10)
# dfj710.insert(1,'Jaccard')

# dfj720 = list(mean_confidence_interval(dfj720))
# dfj720.insert(0,20)
# dfj720.insert(1,'Jaccard')

# dfj730 = list(mean_confidence_interval(dfj730))
# dfj730.insert(0,30)
# dfj730.insert(1,'Jaccard')

# dfj740 = list(mean_confidence_interval(dfj740))
# dfj740.insert(0,40)
# dfj740.insert(1,'Jaccard')

# dfj750 = list(mean_confidence_interval(dfj750))
# dfj750.insert(0,50)
# dfj750.insert(1,'Jaccard')

# dfj760 = list(mean_confidence_interval(dfj760))
# dfj760.insert(0,60)
# dfj760.insert(1,'Jaccard')

# dfj770 = list(mean_confidence_interval(dfj770))
# dfj770.insert(0,70)
# dfj770.insert(1,'Jaccard')



df1 = pd.DataFrame([dfj100, dfj110, dfj120, dfj130, dfj140])#, dfj150, dfj160, dfj170])#, dfj190])
df1.columns = ['k','measurement','mean','lb','ub']
# df2 = pd.DataFrame([dfj200, dfj210, dfj220, dfj230, dfj240])#, dfj250, dfj260, dfj270])#, dfj290])
# df2.columns = ['k','measurement','mean','lb','ub']
# df3 = pd.DataFrame([dfj300, dfj310, dfj320, dfj330, dfj340])#, dfj350, dfj360, dfj370])#, dfj390])
# df3.columns = ['k','measurement','mean','lb','ub']
df4 = pd.DataFrame([dfj400, dfj410, dfj420, dfj430, dfj440])#, dfj450, dfj460, dfj470])#, dfj480])
df4.columns = ['k','measurement','mean','lb','ub']
# df5 = pd.DataFrame([dfj500, dfj510, dfj520, dfj530, dfj540, dfj550, dfj560, dfj570])#, dfj580])
# df5.columns = ['k','measurement','mean','lb','ub']
# df6 = pd.DataFrame([dfj600, dfj610, dfj620, dfj630, dfj640, dfj650, dfj660, dfj670])#, dfj680])
# df6.columns = ['k','measurement','mean','lb','ub']
# df7 = pd.DataFrame([dfj700, dfj710, dfj720, dfj730, dfj740, dfj750, dfj760, dfj770])#, dfj780])
# df7.columns = ['k','measurement','mean','lb','ub']


mean1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'Jaccard'].reset_index()
lb1 = lb1['lb']

# mean2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
# mean2 = mean2['mean']
# ub2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
# ub2 = ub2['ub']
# lb2 = df2[df2['measurement'] == 'Jaccard'].reset_index()
# lb2 = lb2['lb']

# mean3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
# mean3 = mean3['mean']
# ub3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
# ub3 = ub3['ub']
# lb3 = df3[df3['measurement'] == 'Jaccard'].reset_index()
# lb3 = lb3['lb']

mean4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
mean4 = mean4['mean']
ub4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
ub4 = ub4['ub']
lb4 = df4[df4['measurement'] == 'Jaccard'].reset_index()
lb4 = lb4['lb']

# mean5 = df5[df5['measurement'] == 'Jaccard'].reset_index()
# mean5 = mean5['mean']
# ub5 = df5[df5['measurement'] == 'Jaccard'].reset_index()
# ub5 = ub5['ub']
# lb5 = df5[df5['measurement'] == 'Jaccard'].reset_index()
# lb5 = lb5['lb']

# mean6 = df6[df6['measurement'] == 'Jaccard'].reset_index()
# mean6 = mean6['mean']
# ub6 = df6[df6['measurement'] == 'Jaccard'].reset_index()
# ub6 = ub6['ub']
# lb6 = df6[df6['measurement'] == 'Jaccard'].reset_index()
# lb6 = lb6['lb']

# mean7 = df7[df7['measurement'] == 'Jaccard'].reset_index()
# mean7 = mean7['mean']
# ub7 = df7[df7['measurement'] == 'Jaccard'].reset_index()
# ub7 = ub7['ub']
# lb7 = df7[df7['measurement'] == 'Jaccard'].reset_index()
# lb7 = lb7['lb']

# Set some parameters to apply to all plots. These can be overridden
# in each plot if desired
import matplotlib
# Plot size to 14" x 7"
matplotlib.rc('figure', figsize = (15, 9))
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
ax.plot(mean1, lw = 1, color = '#fc7303', alpha = 1, label = 'AVG', marker='x', linestyle=':', linewidth=2, markersize=20)
# ax.plot(mean2, lw = 1, color = '#FF0000', alpha = 1, label = 'SUM', marker='<', linestyle='-.', linewidth=2, markersize=20)
# ax.plot(mean3, lw = 1, color = '#008000', alpha = 1, label = 'AVG+SUM', marker='o', linestyle='--', linewidth=2, markersize=20)
ax.plot(mean4, lw = 1, color = '#0000FF', alpha = 1, label = 'MAX', marker='+', linestyle=':', linewidth=2, markersize=20)
# ax.plot(mean5, lw = 1, color = '#800000', alpha = 1, label = 'Num of Suicides', marker='*', linestyle='-', linewidth=2, markersize=20)
# ax.plot(mean6, lw = 1, color = '#3e6980', alpha = 1, label = 'Suicides per 100k Pop', marker='>', linestyle='-.', linewidth=2, markersize=20)
# ax.plot(mean7, lw = 1, color = '#000000', alpha = 1, label = 'No Impute', marker='s', linestyle='--', linewidth=2, markersize=20)



# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#dedddc', alpha = 0.4)
# ax.fill_between(t, lb2, ub2, color = '#dedddc', alpha = 0.4)
# ax.fill_between(t, lb3, ub3, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb4, ub4, color = '#dedddc', alpha = 0.4)
# ax.fill_between(t, lb5, ub5, color = '#dedddc', alpha = 0.4)
# ax.fill_between(t, lb6, ub6, color = '#dedddc', alpha = 0.4)
# ax.fill_between(t, lb7, ub7, color = '#dedddc', alpha = 0.4)




# Label the axes and provide a title
#ax.set_title("Impact missing on Effectiveness (RBO), 95% CI, k = 10")
ax.set_xlabel("percentage of missing data")
ax.set_ylabel("Effectiveness - random imputation")
x = [0, 5, 10, 15, 20]#, 50, 60, 70]#, 90]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0)
ax.set_ylim(ymax=1.02)

ax.legend(frameon=False, loc='best')

plt.savefig(''+ output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('' + output_plot + '.png')
plt.show()
