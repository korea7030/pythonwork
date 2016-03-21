# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:44:42 2016

@author: Administrator
"""

import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/glass/glass.data")

glass = pd.read_csv(target_url, header = None, prefix="V")
glass.columns = ['Id', 'RI', 'Na', 'Mg', 'Al', 'Si', 'K', 'Ca', 'Ba', 'Fe', 'Type']

print (glass.head())

# 요약 통계량 생성 
summary = glass.describe()
print(summary)

ncol1 = len(glass.columns)

glassNormalized = glass.iloc[:, 1:ncol1]
ncol2 = len(glassNormalized.columns)
summary2 = glassNormalized.describe()

for i in range(ncol2):
    mean = summary2.iloc[1,i]
    sd = summary2.iloc[2,i]
    
    glassNormalized.iloc[:, i:(i+1)] = (glassNormalized.iloc[:, i:(i+1)]-mean)/sd

array = glassNormalized.values
plot.boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges - Normalized "))
plot.show()
