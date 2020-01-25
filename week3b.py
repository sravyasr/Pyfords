# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:13:02 2019

@author: sri
"""

import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print(s)

t = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])
print(t[:3])

#DataFrame
print("DataFrame :")
import pandas as pd
df = pd.DataFrame()
print(df)

data = [1,2]
df = pd.DataFrame(data)
print(df)

data = [['Alex',10],['Bob',12],['Clarke',13]]
data = {'Name':['Tom', 'Jack', 'Steve'],'Age':[28,34,29]}
df = pd.DataFrame(data)
print(df)

data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)
df2 = df2.drop('first')

print(df2)