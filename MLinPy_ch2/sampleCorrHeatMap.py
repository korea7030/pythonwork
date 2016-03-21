# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 15:28:38 2016

@author: Administrator

히트맵으로 상관관계 확인하기 
  - 대각선에 가까울 수록 각 변수가 서로 상관관계가 있다고 봄
"""

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

# 바위와 기뢰 데이터를 읽어 pandas 데이터 프레임으로 변환
rocksVMines = pd.read_csv(target_url, header=None, prefix="V")

# 수치형 속성 간 상관관계 계산 
corrMat = DataFrame(rocksVMines.corr())

# 히트 맵을 이용하여 상관관계 시각화
plot.pcolor(corrMat)
plot.show()