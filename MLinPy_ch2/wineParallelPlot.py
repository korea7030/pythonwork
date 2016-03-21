# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:24:47 2016

@author: Administrator
"""

import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot
from math import exp

target_url = "http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv"
wine = pd.read_csv(target_url, header=0, sep=";")

# 전체 버전을 가지도록 컬럼 이름 프린트 
summary = wine.describe()
nrows = len(wine.index)
tasteCol = len(summary.columns)
meanTaste = summary.iloc[1,tasteCol-1]
sdTaste = summary.iloc[2, tasteCol-1]
nDataCol = len(wine.columns)-1

for i in range(nrows):
    # 연속된 데이터 처럼 데이터 행으로 도표 
    dataRow = wine.iloc[i,1:nDataCol]
    normTarget = (wine.iloc[i, nDataCol] - meanTaste) / sdTaste
    labelColor = 1.0/(1.0+exp(-normTarget))
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel(("Attribute Values"))
plot.show()

wineNormalized = wine
ncols = len(wineNormalized.columns)

for i in range(ncols):
    mean = summary.iloc[1,i]
    sd = summary.iloc[2,i]
    wineNormalized.iloc[:, i:(i+1)] = (wineNormalized.iloc[:, i:(i+1)] - mean) / sd

# 정규화된 값으로 다시 수행
for i in range(nrows):
    dataRow = wineNormalized.iloc[i,1:nDataCol]
    normTarget = wineNormalized.iloc[i,nDataCol]
    labelColor = 1.0/(1.0+exp(-normTarget))
    dataRow.plot(color=plot.cm.RdYlBu(labelColor), alpha=0.5)

plot.xlabel("Attribute Index")
plot.ylabel(("Attribute Values"))
plot.show()
