# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:43:25 2016

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plot
from random import uniform
target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# 바위와 기뢰 데이터를 읽어 pandas 데이터 프레임으로 변환
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")
# print (rocksVMines) 
# 타겟을 수치형으로 변환
target = []

for i in range(208):
    #"M" 또는 "R" 레이블에 따라 0 또는 1 타깃 값을 부여
    if rocksVMines.iat[i,60] == "M":
        target.append(1.0)
    else:
        target.append(0.0)

# 35번째 속성으로 도표 그리기 
dataRow = rocksVMines.iloc[0:208, 35] # 35 속성의 208 row

# print (dataRow)
# print (dataRow == dataRow1)
# print (dataRow1)
plot.scatter(dataRow, target)

plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()

## 시각화 개선(점을 흔들리게 하였고, 투명하게 만듦)
target = []
for i in range(208):
    if rocksVMines.iat[i,60] == "M":
        target.append(1.0+uniform(-0.1, 0.1)) # 임의의 값을 더함
    else:
        target.append(0.0+uniform(-0.1, 0.1)) # 임의의 값을 더함
    
dataRow = rocksVMines.iloc[0:208, 35]
plot.scatter(dataRow, target, alpha=0.5, s=120)
plot.xlabel("Attribute Value")
plot.ylabel("Target Value")
plot.show()
