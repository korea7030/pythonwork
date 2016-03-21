# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:43:25 2016

@author: Administrator
"""

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot
from math import exp

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

# 전복 데이터 읽기
abalone = pd.read_csv(target_url, header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

# 스케일링에 사용하기 위해 통계량 구하기
summary = abalone.describe()
minRings = summary.iloc[3,7]
maxRings = summary.iloc[7,7]
nrows = len(abalone.index)

for i in range(nrows):
    # 연속된 데이터처럼 데이터 행으로 도표 
    dataRow = abalone.iloc[i,1:8]
    labelColor = (abalone.iloc[i,8] - minRings) / (maxRings - minRings)
    dataRow.plot(color=plot.cm.RdYlBu(labelColor) , alpha = 0.5)

plot.xlabel("Attribute Index")
plot.ylabel(("Attribute Values"))
plot.show()

# 평균과 표준편차로 다시 정규화, 이후 로짓 함수로 압축
meanRings = summary.iloc[1,7]
sdRings = summary.iloc[2,7]

for i in range(nrows) :
    # 연속된 데이터처럼 데이터 행으로 도표 
    dataRow = abalone.iloc[i,1:8]
    labelColor = (abalone.iloc[i,8] - meanRings) / sdRings
    dataRow.plot(color=plot.cm.RdYlBu(labelColor) , alpha = 0.5)

plot.xlabel("Attribute Index")
plot.ylabel(("Attribute values"))
plot.show()
