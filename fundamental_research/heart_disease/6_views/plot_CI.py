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

input_file1 = 'results/avg_oldpeak_distance.csv'
input_file2 = 'results/max_oldpeak_distance.csv'

input_file3 = 'results/sum_oldpeak_distance.csv'

input_file4 = 'results/avg_chol_distance.csv'
input_file5 = 'results/max_chol_distance.csv'

input_file6 = 'results/sum_chol_distance.csv'

input_file7 = 'results/count_chol_distance.csv'
input_file8 = 'results/count_oldpeak_distance.csv'




output_plot = 'distance_all_6'


# ===============================================================
# IDEAL VS STANDARD
df = pd.read_csv(input_file1, names=['percentage','dist'])
df = df.dropna()

dfj100 = df[(df['percentage'] == 0)]
dfj100 = dfj100['dist']

dfj110 = df[(df['percentage'] == 5)]
dfj110 = dfj110['dist']

dfj120 = df[(df['percentage'] == 10)]
dfj120 = dfj120['dist']

dfj130 = df[(df['percentage'] == 15)]
dfj130 = dfj130['dist']

dfj140 = df[(df['percentage'] == 20)]
dfj140 = dfj140['dist']

dfj150 = df[(df['percentage'] == 25)]
dfj150 = dfj150['dist']

dfj160 = df[(df['percentage'] == 30)]
dfj160 = dfj160['dist']







dfj100 = list(mean_confidence_interval(dfj100))
dfj100.insert(0,0)
dfj100.insert(1,'dist')

dfj110 = list(mean_confidence_interval(dfj110))
dfj110.insert(0,5)
dfj110.insert(1,'dist')

dfj120 = list(mean_confidence_interval(dfj120))
dfj120.insert(0,10)
dfj120.insert(1,'dist')

dfj130 = list(mean_confidence_interval(dfj130))
dfj130.insert(0,15)
dfj130.insert(1,'dist')

dfj140 = list(mean_confidence_interval(dfj140))
dfj140.insert(0,20)
dfj140.insert(1,'dist')

dfj150 = list(mean_confidence_interval(dfj150))
dfj150.insert(0,25)
dfj150.insert(1,'dist')

dfj160 = list(mean_confidence_interval(dfj160))
dfj160.insert(0,30)
dfj160.insert(1,'dist')


df = pd.read_csv(input_file2, names=['percentage','dist'])
df = df.dropna()


dfj200 = df[(df['percentage'] == 0)]
dfj200 = dfj200['dist']

dfj210 = df[(df['percentage'] == 5)]
dfj210 = dfj210['dist']

dfj220 = df[(df['percentage'] == 10)]
dfj220 = dfj220['dist']

dfj230 = df[(df['percentage'] == 15)]
dfj230 = dfj230['dist']

dfj240 = df[(df['percentage'] == 20)]
dfj240 = dfj240['dist']

dfj250 = df[(df['percentage'] == 25)]
dfj250 = dfj250['dist']

dfj260 = df[(df['percentage'] == 30)]
dfj260 = dfj260['dist']

# dfj270 = df[(df['percentage'] == 70)]
# dfj270 = dfj270['Cumulative_distance']



dfj200 = list(mean_confidence_interval(dfj200))
dfj200.insert(0,0)
dfj200.insert(1,'dist')

dfj210 = list(mean_confidence_interval(dfj210))
dfj210.insert(0,5)
dfj210.insert(1,'dist')

dfj220 = list(mean_confidence_interval(dfj220))
dfj220.insert(0,10)
dfj220.insert(1,'dist')

dfj230 = list(mean_confidence_interval(dfj230))
dfj230.insert(0,15)
dfj230.insert(1,'dist')

dfj240 = list(mean_confidence_interval(dfj240))
dfj240.insert(0,20)
dfj240.insert(1,'dist')

dfj250 = list(mean_confidence_interval(dfj250))
dfj250.insert(0,25)
dfj250.insert(1,'dist')

dfj260 = list(mean_confidence_interval(dfj260))
dfj260.insert(0,30)
dfj260.insert(1,'dist')

# dfj270 = list(mean_confidence_interval(dfj270))
# dfj270.insert(0,70)
# dfj270.insert(1,'Cumulative_distance')

df = pd.read_csv(input_file3, names=['percentage','dist'])
df = df.dropna()

dfj300 = df[(df['percentage'] == 0)]
dfj300 = dfj300['dist']

dfj310 = df[(df['percentage'] == 5)]
dfj310 = dfj310['dist']

dfj320 = df[(df['percentage'] == 10)]
dfj320 = dfj320['dist']

dfj330 = df[(df['percentage'] == 15)]
dfj330 = dfj330['dist']

dfj340 = df[(df['percentage'] == 20)]
dfj340 = dfj340['dist']

dfj350 = df[(df['percentage'] == 25)]
dfj350 = dfj350['dist']

dfj360 = df[(df['percentage'] == 30)]
dfj360 = dfj360['dist']







dfj300 = list(mean_confidence_interval(dfj300))
dfj300.insert(0,0)
dfj300.insert(1,'dist')

dfj310 = list(mean_confidence_interval(dfj310))
dfj310.insert(0,5)
dfj310.insert(1,'dist')

dfj320 = list(mean_confidence_interval(dfj320))
dfj320.insert(0,10)
dfj320.insert(1,'dist')

dfj330 = list(mean_confidence_interval(dfj330))
dfj330.insert(0,15)
dfj330.insert(1,'dist')

dfj340 = list(mean_confidence_interval(dfj340))
dfj340.insert(0,20)
dfj340.insert(1,'dist')

dfj350 = list(mean_confidence_interval(dfj350))
dfj350.insert(0,25)
dfj350.insert(1,'dist')

dfj360 = list(mean_confidence_interval(dfj360))
dfj360.insert(0,30)
dfj360.insert(1,'dist')


df = pd.read_csv(input_file4, names=['percentage','dist'])
df = df.dropna()


dfj400 = df[(df['percentage'] == 0)]
dfj400 = dfj400['dist']

dfj410 = df[(df['percentage'] == 5)]
dfj410 = dfj410['dist']

dfj420 = df[(df['percentage'] == 10)]
dfj420 = dfj420['dist']

dfj430 = df[(df['percentage'] == 15)]
dfj430 = dfj430['dist']

dfj440 = df[(df['percentage'] == 20)]
dfj440 = dfj440['dist']

dfj450 = df[(df['percentage'] == 25)]
dfj450 = dfj450['dist']

dfj460 = df[(df['percentage'] == 30)]
dfj460 = dfj460['dist']

# dfj470 = df[(df['percentage'] == 70)]
# dfj470 = dfj470['Cumulative_distance']



dfj400 = list(mean_confidence_interval(dfj400))
dfj400.insert(0,0)
dfj400.insert(1,'dist')

dfj410 = list(mean_confidence_interval(dfj410))
dfj410.insert(0,5)
dfj410.insert(1,'dist')

dfj420 = list(mean_confidence_interval(dfj420))
dfj420.insert(0,10)
dfj420.insert(1,'dist')

dfj430 = list(mean_confidence_interval(dfj430))
dfj430.insert(0,15)
dfj430.insert(1,'dist')

dfj440 = list(mean_confidence_interval(dfj440))
dfj440.insert(0,20)
dfj440.insert(1,'dist')

dfj450 = list(mean_confidence_interval(dfj450))
dfj450.insert(0,25)
dfj450.insert(1,'dist')

dfj460 = list(mean_confidence_interval(dfj460))
dfj460.insert(0,30)
dfj460.insert(1,'dist')


df = pd.read_csv(input_file5, names=['percentage','dist'])
df = df.dropna()

dfj500 = df[(df['percentage'] == 0)]
dfj500 = dfj500['dist']

dfj510 = df[(df['percentage'] == 5)]
dfj510 = dfj510['dist']

dfj520 = df[(df['percentage'] == 10)]
dfj520 = dfj520['dist']

dfj530 = df[(df['percentage'] == 15)]
dfj530 = dfj530['dist']

dfj540 = df[(df['percentage'] == 20)]
dfj540 = dfj540['dist']

dfj550 = df[(df['percentage'] == 25)]
dfj550 = dfj550['dist']

dfj560 = df[(df['percentage'] == 30)]
dfj560 = dfj560['dist']







dfj500 = list(mean_confidence_interval(dfj500))
dfj500.insert(0,0)
dfj500.insert(1,'dist')

dfj510 = list(mean_confidence_interval(dfj510))
dfj510.insert(0,5)
dfj510.insert(1,'dist')

dfj520 = list(mean_confidence_interval(dfj520))
dfj520.insert(0,10)
dfj520.insert(1,'dist')

dfj530 = list(mean_confidence_interval(dfj530))
dfj530.insert(0,15)
dfj530.insert(1,'dist')

dfj540 = list(mean_confidence_interval(dfj540))
dfj540.insert(0,20)
dfj540.insert(1,'dist')

dfj550 = list(mean_confidence_interval(dfj550))
dfj550.insert(0,25)
dfj550.insert(1,'dist')

dfj560 = list(mean_confidence_interval(dfj560))
dfj560.insert(0,30)
dfj560.insert(1,'dist')


df = pd.read_csv(input_file6, names=['percentage','dist'])
df = df.dropna()


dfj600 = df[(df['percentage'] == 0)]
dfj600 = dfj600['dist']

dfj610 = df[(df['percentage'] == 5)]
dfj610 = dfj610['dist']

dfj620 = df[(df['percentage'] == 10)]
dfj620 = dfj620['dist']

dfj630 = df[(df['percentage'] == 15)]
dfj630 = dfj630['dist']

dfj640 = df[(df['percentage'] == 20)]
dfj640 = dfj640['dist']

dfj650 = df[(df['percentage'] == 25)]
dfj650 = dfj650['dist']

dfj660 = df[(df['percentage'] == 30)]
dfj660 = dfj660['dist']

# dfj670 = df[(df['percentage'] == 70)]
# dfj670 = dfj670['Cumulative_distance']



dfj600 = list(mean_confidence_interval(dfj600))
dfj600.insert(0,0)
dfj600.insert(1,'dist')

dfj610 = list(mean_confidence_interval(dfj610))
dfj610.insert(0,5)
dfj610.insert(1,'dist')

dfj620 = list(mean_confidence_interval(dfj620))
dfj620.insert(0,10)
dfj620.insert(1,'dist')

dfj630 = list(mean_confidence_interval(dfj630))
dfj630.insert(0,15)
dfj630.insert(1,'dist')

dfj640 = list(mean_confidence_interval(dfj640))
dfj640.insert(0,20)
dfj640.insert(1,'dist')

dfj650 = list(mean_confidence_interval(dfj650))
dfj650.insert(0,25)
dfj650.insert(1,'dist')

dfj660 = list(mean_confidence_interval(dfj660))
dfj660.insert(0,30)
dfj660.insert(1,'dist')


df = pd.read_csv(input_file7, names=['percentage','dist'])
df = df.dropna()

dfj700 = df[(df['percentage'] == 0)]
dfj700 = dfj700['dist']

dfj710 = df[(df['percentage'] == 5)]
dfj710 = dfj710['dist']

dfj720 = df[(df['percentage'] == 10)]
dfj720 = dfj720['dist']

dfj730 = df[(df['percentage'] == 15)]
dfj730 = dfj730['dist']

dfj740 = df[(df['percentage'] == 20)]
dfj740 = dfj740['dist']

dfj750 = df[(df['percentage'] == 25)]
dfj750 = dfj750['dist']

dfj760 = df[(df['percentage'] == 30)]
dfj760 = dfj760['dist']







dfj700 = list(mean_confidence_interval(dfj700))
dfj700.insert(0,0)
dfj700.insert(1,'dist')

dfj710 = list(mean_confidence_interval(dfj710))
dfj710.insert(0,5)
dfj710.insert(1,'dist')

dfj720 = list(mean_confidence_interval(dfj720))
dfj720.insert(0,10)
dfj720.insert(1,'dist')

dfj730 = list(mean_confidence_interval(dfj730))
dfj730.insert(0,15)
dfj730.insert(1,'dist')

dfj740 = list(mean_confidence_interval(dfj740))
dfj740.insert(0,20)
dfj740.insert(1,'dist')

dfj750 = list(mean_confidence_interval(dfj750))
dfj750.insert(0,25)
dfj750.insert(1,'dist')

dfj760 = list(mean_confidence_interval(dfj760))
dfj760.insert(0,30)
dfj760.insert(1,'dist')


df = pd.read_csv(input_file8, names=['percentage','dist'])
df = df.dropna()


dfj800 = df[(df['percentage'] == 0)]
dfj800 = dfj800['dist']

dfj810 = df[(df['percentage'] == 5)]
dfj810 = dfj810['dist']

dfj820 = df[(df['percentage'] == 10)]
dfj820 = dfj820['dist']

dfj830 = df[(df['percentage'] == 15)]
dfj830 = dfj830['dist']

dfj840 = df[(df['percentage'] == 20)]
dfj840 = dfj840['dist']

dfj850 = df[(df['percentage'] == 25)]
dfj850 = dfj850['dist']

dfj860 = df[(df['percentage'] == 30)]
dfj860 = dfj860['dist']

# dfj870 = df[(df['percentage'] == 70)]
# dfj870 = dfj870['Cumulative_distance']



dfj800 = list(mean_confidence_interval(dfj800))
dfj800.insert(0,0)
dfj800.insert(1,'dist')

dfj810 = list(mean_confidence_interval(dfj810))
dfj810.insert(0,5)
dfj810.insert(1,'dist')

dfj820 = list(mean_confidence_interval(dfj820))
dfj820.insert(0,10)
dfj820.insert(1,'dist')

dfj830 = list(mean_confidence_interval(dfj830))
dfj830.insert(0,15)
dfj830.insert(1,'dist')

dfj840 = list(mean_confidence_interval(dfj840))
dfj840.insert(0,20)
dfj840.insert(1,'dist')

dfj850 = list(mean_confidence_interval(dfj850))
dfj850.insert(0,25)
dfj850.insert(1,'dist')

dfj860 = list(mean_confidence_interval(dfj860))
dfj860.insert(0,30)
dfj860.insert(1,'dist')



df1 = pd.DataFrame([dfj100, dfj110, dfj120, dfj130, dfj140, dfj150, dfj160])#, dfj190])
df1.columns = ['percentage','measurement','mean','lb','ub']
df2 = pd.DataFrame([dfj200, dfj210, dfj220, dfj230, dfj240, dfj250, dfj260])#, dfj290])
df2.columns = ['percentage','measurement','mean','lb','ub']
#print(df1)
df3 = pd.DataFrame([dfj300, dfj310, dfj320, dfj330, dfj340, dfj350, dfj360])#, dfj390])
df3.columns = ['percentage','measurement','mean','lb','ub']
df4 = pd.DataFrame([dfj400, dfj410, dfj420, dfj430, dfj440, dfj450, dfj460])#, dfj490])
df4.columns = ['percentage','measurement','mean','lb','ub']

df5 = pd.DataFrame([dfj500, dfj510, dfj520, dfj530, dfj540, dfj550, dfj560])#, dfj590])
df5.columns = ['percentage','measurement','mean','lb','ub']
df6 = pd.DataFrame([dfj600, dfj610, dfj620, dfj630, dfj640, dfj650, dfj660])#, dfj690])
df6.columns = ['percentage','measurement','mean','lb','ub']


df7 = pd.DataFrame([dfj700, dfj710, dfj720, dfj730, dfj740, dfj750, dfj760])#, dfj790])
df7.columns = ['percentage','measurement','mean','lb','ub']
df8 = pd.DataFrame([dfj800, dfj810, dfj820, dfj830, dfj840, dfj850, dfj860])#, dfj890])
df8.columns = ['percentage','measurement','mean','lb','ub']





mean1 = df1[df1['measurement'] == 'dist'].reset_index()
mean1 = mean1['mean']
ub1 = df1[df1['measurement'] == 'dist'].reset_index()
ub1 = ub1['ub']
lb1 = df1[df1['measurement'] == 'dist'].reset_index()
lb1 = lb1['lb']

mean2 = df2[df2['measurement'] == 'dist'].reset_index()
mean2 = mean2['mean']
ub2 = df2[df2['measurement'] == 'dist'].reset_index()
ub2 = ub2['ub']
lb2 = df2[df2['measurement'] == 'dist'].reset_index()
lb2 = lb2['lb']

mean3 = df3[df3['measurement'] == 'dist'].reset_index()
mean3 = mean3['mean']
ub3 = df3[df3['measurement'] == 'dist'].reset_index()
ub3 = ub3['ub']
lb3 = df3[df3['measurement'] == 'dist'].reset_index()
lb3 = lb3['lb']

mean4 = df4[df4['measurement'] == 'dist'].reset_index()
mean4 = mean4['mean']
ub4 = df4[df4['measurement'] == 'dist'].reset_index()
ub4 = ub4['ub']
lb4 = df4[df4['measurement'] == 'dist'].reset_index()
lb4 = lb4['lb']


mean5 = df5[df5['measurement'] == 'dist'].reset_index()
mean5 = mean5['mean']
ub5 = df5[df5['measurement'] == 'dist'].reset_index()
ub5 = ub5['ub']
lb5 = df5[df5['measurement'] == 'dist'].reset_index()
lb5 = lb5['lb']

mean6 = df6[df6['measurement'] == 'dist'].reset_index()
mean6 = mean6['mean']
ub6 = df6[df6['measurement'] == 'dist'].reset_index()
ub6 = ub6['ub']
lb6 = df6[df6['measurement'] == 'dist'].reset_index()
lb6 = lb6['lb']


mean7 = df7[df7['measurement'] == 'dist'].reset_index()
mean7 = mean7['mean']
ub7 = df7[df7['measurement'] == 'dist'].reset_index()
ub7 = ub7['ub']
lb7 = df7[df7['measurement'] == 'dist'].reset_index()
lb7 = lb7['lb']

mean8 = df8[df8['measurement'] == 'dist'].reset_index()
mean8 = mean8['mean']
ub8 = df8[df8['measurement'] == 'dist'].reset_index()
ub8 = ub8['ub']
lb8 = df8[df8['measurement'] == 'dist'].reset_index()
lb8 = lb8['lb']


#print(df1)
df1.to_csv('df1.csv',index=False)
df2.to_csv('df2.csv',index=False)

df3.to_csv('df3.csv',index=False)
df4.to_csv('df4.csv',index=False)

df5.to_csv('df5.csv',index=False)
df6.to_csv('df6.csv',index=False)

df7.to_csv('df7.csv',index=False)
df8.to_csv('df8.csv',index=False)
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


#print(mean1)

t = np.arange(len(mean1))

_, ax = plt.subplots()
# Plot the data, set the linewidth, color and transparency of the
# line, provide a label for the legend
ax.plot(mean1, lw = 1, color = '#fc7303', alpha = 1, label = 'disease_AVG_oldpeak', marker='x', linestyle=':', linewidth=2, markersize=20)
ax.plot(mean2, lw = 1, color = '#FF0000', alpha = 1, label = 'disease_MAX_oldpeak', marker='<', linestyle='-.', linewidth=2, markersize=20)
ax.plot(mean3, lw = 1, color = '#008000', alpha = 1, label = 'disease_SUM_oldpeak', marker='o', linestyle='--', linewidth=2, markersize=20)
ax.plot(mean8, lw = 1, color = '#000000', alpha = 1, label = 'disease_COUNT_*', marker='s', linestyle='--', linewidth=2, markersize=20)
ax.plot(mean4, lw = 1, color = '#0000FF', alpha = 1, label = 'restchag_AVG_chol', marker='+', linestyle=':', linewidth=2, markersize=20)
ax.plot(mean5, lw = 1, color = '#800000', alpha = 1, label = 'restecg_MAX_chol', marker='*', linestyle='-', linewidth=2, markersize=20)
ax.plot(mean6, lw = 1, color = '#3e6980', alpha = 1, label = 'restecg_SUM_chol', marker='>', linestyle='-.', linewidth=2, markersize=20)
ax.plot(mean7, lw = 1, color = '#e32db0', alpha = 1, label = 'restecg_COUNT_*', marker='^', linestyle='-.', linewidth=2, markersize=20)



# Shade the confidence interval
ax.fill_between(t, lb1, ub1, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb2, ub2, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb3, ub3, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb4, ub4, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb5, ub5, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb6, ub6, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb7, ub7, color = '#dedddc', alpha = 0.4)
ax.fill_between(t, lb8, ub8, color = '#dedddc', alpha = 0.4)




# Label the axes and provide a title
#ax.set_title("Euclidean distance between Viz from complete and incomplete data, 1 mean exactly same, 95% CI, k = 10")
ax.set_xlabel("percentage of missing data")
ax.set_ylabel("Distance between viz of complete vs incomplete")
x = [0, 5, 10, 15, 20, 25, 30]#, 90]
xi = list(range(len(x)))
plt.xticks(xi, x)
# Display legend
ax.set_ylim(ymin=0.8)
ax.set_ylim(ymax=1.02)

ax.legend(frameon=False, loc='best')

plt.savefig(''+ output_plot + '.svg', format="svg", dpi = 1000)
plt.savefig('' + output_plot + '.png')
plt.show()
