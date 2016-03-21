# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 14:30:27 2016

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# 바위와 기뢰 데이터를 읽어 pandas 데이터 프레임으로 변환
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

# 수치형 속성 간 상관관계 계산
dataRow2 = rocksVMines.iloc[1,0:60] # 두번째 row의 60개 속성
dataRow3 = rocksVMines.iloc[2,0:60] # 세번째 row의 60개 속성

print ("dataRow2 : \n"+str(dataRow2))
print ("dataRow3 : \n"+str(dataRow3))

plot.scatter(dataRow2, dataRow3)
plot.xlabel("2nd Attribute")
plot.ylabel(("3rd Attribute"))
plot.show()

dataRow21 = rocksVMines.iloc[20,0:60] # 21번째 row의 60개 속성
print ("dataRow21 : \n"+str(dataRow21))

plot.scatter(dataRow2, dataRow21)

plot.xlabel("2nd Attribute")
plot.ylabel(("21st Attribute"))
plot.show()
