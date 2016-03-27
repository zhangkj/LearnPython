#-*-encoding:utf-8-*-

import  pandas as pd
import  numpy as np
#===============pandas库中数据的筛选与过滤
s = pd.Series([1,3,5,np.nan,6])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df2 = pd.DataFrame({'A':1.,
                    'B':np.array([3] * 4,dtype='int32'),
                    'C':'foo'})
df2.dtypes

df.head()
df.head(3)
df.tail()
df.tail(3)
df.index
df.columns
df.values
df.describe()
df.T
df.sort_index(axis=1, ascending=False)         #列轴，正反排序
df.sort_values(by='B')
df.sort_values(by='B',ascending=False)
df.sort(columns="B")
df['A']
df[0:3]
df['20130102':'20130104']
df.loc[:,['A','B']]
df.loc['20130102':'20130104',['A','B']]
df.loc['20130102',['A','B']]
df.loc[dates[0],'A']
df.at[dates[0],'A']
print

#================pandas中字符串的提取与操作
#s = pd.Series(list("ABcD"))
s = pd.Series(["A1","a2","a3","b4"])
s.str.lower()
s.str.upper()
s.str.len()
s.str.split('')
s.str.isalpha()
s.str.replace('A','a')

s.str.extract("[b](\d)")    #提取
s.str.extract("([b])(\d)")
s.str.extract("(?P<str>[b])(?P<digit>\d)")
s = pd.Series(["a","B","c","d"])
pattern = r'[a-z]'
s.str.contains(pattern)
patter = r'[A-Za-z]'
s.str.contains(pattern)
s.str.match('a')
s.str.contains('^a')      #以a开头
s.str.startswith('a')    #以a开头
s.str.contains('a$')      #以a结束
s.str.endswith('a')      #以a结束
