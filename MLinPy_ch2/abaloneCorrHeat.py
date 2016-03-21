# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 16:57:06 2016

@author: Administrator

전복 데이터 상관관계 히트맵 시각화
"""

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

# 전복 데이터 읽기
abalone = pd.read_csv(target_url, header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

# 상관관계 매트릭스 계산
corMat = DataFrame(abalone.iloc[:,1:9].corr())
# 상관관계 매트릭스 프린트
print (corMat)

# 히트맵을 이용한 상관관계 시각화
plot.pcolor(corMat)
plot.show()
