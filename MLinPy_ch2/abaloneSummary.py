# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:49:35 2016

@author: Administrator

전복 데이터 세트를 읽어 들이고 요약하기
"""
import pandas as pd
from pandas import DataFrame
from pylab import *
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data")

# 전복 데이터 읽기
abalone = pd.read_csv(target_url, header=None, prefix="V")
abalone.columns = ['Sex', 'Length', 'Diameter', 'Height', 'Whole weight', 'Shucked weight', 'Viscera weight', 'Shell weight', 'Rings']

print (abalone.head())
print (abalone.tail())

# 데이터 프레임의 요약 통계량 프린트 
summary = abalone.describe()
print (summary)

# 수치형 속성의 상자 도표 
# 도표 루틴을 사용하기 위해 array로 변환 
array = abalone.iloc[:,1:9].values
print ("plot 1 \n")
plot.boxplot(array)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))
plot.show()

# 최종 컬럼(나이테)은 스케일이 나머지 컬럼과 다름
# - 제외 후 도표를 다시 그림
array2 = abalone.iloc[:,1:8].values
print ("plot 2 \n")
plot.boxplot(array2)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges"))
plot.show()

# 제외한 결과는 좋지만 변수를 다시 정규화 하면 일반화가 더 나을 것임.
# 컬럼을 평균 0과 단위 표준편차로 정규화
# 일반적인 정규화 형태
abaloneNormalized = abalone.iloc[:,1:9]

for i in range(8):
    mean = summary.iloc[1,i] # 요약통계량 에서 각 속성의 평균만 뽑음
    sd = summary.iloc[2,i]   # 요약통계량 에서 각 속성의 표준편차만 뽑음 
    abaloneNormalized.iloc[:,i:(i+1)] = (abaloneNormalized.iloc[:, i:(i+1)]-mean) / sd

array3 = abaloneNormalized.values
print ("plot 3 \n")
plot.boxplot(array3)
plot.xlabel("Attribute Index")
plot.ylabel(("Quartile Ranges - Normalized "))
plot.show()


