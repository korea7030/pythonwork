# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:13:07 2016

@author: Administrator
"""

import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv")
wine = pd.read_csv(target_url, header = 0, sep=";")

print (wine.head())

# 요약통계량 생성
summary = wine.describe()
print (summary)

wineNormalized = wine
ncols = len(wineNormalized.columns)

for i in range(ncols):
    mean = summary.iloc[1,i]
    sd = summary.iloc[2,i]
    
    wineNormalized.iloc[:,i:(i+1)] = (wineNormalized.iloc[:,i:(i+1)]-mean) / sd
    
array = wineNormalized.values
plot.boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges - Normalized"))
plot.show()
