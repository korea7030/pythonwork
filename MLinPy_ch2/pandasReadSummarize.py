# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:20:27 2016

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# 바위와 기뢰 데이터를 읽어 pandas 데이터 프레임으로 변환
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

# 데이터 프레임의 헤더와 테일 프린트
print(rocksVMines.head())
print(rocksVMines.tail())

# 데이터 프레임의 요약 통계량 프린트
summary = rocksVMines.describe()
print (summary)

# 그래프 출력
for i in range(208):
    # "M" 또는 "R" 레이블에 따라 색깔 지정
    if rocksVMines.iat[i,60] == "M":
        pcolor = "red"
    else :
        pcolor = "blue"
    
    # 연속된 데이터처럼 데이터 행으로 도표 그리기
    dataRow = rocksVMines.iloc[i,0:60]
    dataRow.plot(color=pcolor)

plot.xlabel("Attribute Index")
plot.ylabel(("Attribute Values"))
plot.show()
