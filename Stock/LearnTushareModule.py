
#-*-encoding:utf-8_*-

import tushare as ts
import pandas as pd
import  matplotlib
import matplotlib.pyplot as plt

#===============数据绘图
codeNum = '600415'
startDate = '2015-04-01'
endDate = '2015-06-18'
#df = ts.get_tick_data(codeNum,startDate)
#print df


df = ts.get_h_data(codeNum,start=startDate,end=endDate)
print df

#所有的结果绘图
df.plot()

df.high.plot()

with pd.plot_params.use('x_compat',True):
    df.open.plot(color='g')
    df.close.plot(color='y')
    df.high.plot(color='r')
    df.low.plot(color='b')
plt.show()
with pd.plot_params.use('x_compat',True):
    df.high.plot(color='r',figsize=(10,4),grid='on')
    df.low.plot(color='b',figsize=(10,4),grid='on')
print 1
plt.show()

#保存图片
fig = plt.gcf()
df = ts.get_h_data(codeNum,startDate,endDate)
with pd.plot_params.use('x_compat', True):
    df.high.plot(color='r',figsize=(10,4),grid='on')
    df.low.plot(color='b',figsize=(10,4),grid='on')
    fig.savefig('graph.png')