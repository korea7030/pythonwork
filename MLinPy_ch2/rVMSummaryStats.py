# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 15:09from urllib.request import urlopen
:18 2016

@author: Administrator
"""

# import urllib2
import urllib2
import sys
import numpy as np

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib2.urlopen(target_url)

xList = []
labels = []
for line in data:
    row = line.strip().split(',')
    xList.append(row)
    

nrow = len(xList)
ncol = len(xList[1])

print (ncol)

type = [0]*3
colCounts = []

# 세번째 컬럼에 대한 통계량
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))

colArray = np.array(colData)
colMean = np.mean(colArray)
colsd = np.std(colArray)
sys.stdout.write("Mean = "+'\t'+str(colMean)+'\t\t'+"Standard Deviation = "+ '\t '+str(colsd)+"\n")

# 분위수 경계 계산
ntiles = 4

percentBdry = []
for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

sys.stdout.write("\nBoundaries for 4 Equal Percentiles \n")
print (percentBdry)
sys.stdout.write(" \n")

# 10 개의 동일한 간격으로 수행 
ntiles = 10

percentBrdy = []

for i in range(ntiles+1):
    percentBdry.append(np.percentile(colArray, i*(100)/ntiles))

sys.stdout.write("Boundaries for 10 Equal Percentiles \n")
print (percentBdry)
sys.stdout.write(" \n")

# 최종 컬럼에는 범주형 변수가 포함 
col = 60
colData = []
for row in xList:
    colData.append(row[col])

unique = set(colData)
sys.stdout.write("Unique Label Values \n")
print (unique)

# 개별 값이 있는 요소의 수를 오름 셈
catDict = dict(zip(list(unique), range(len(unique))))

catCount = [0]*2

for elt in colData:
    catCount[catDict[elt]] += 1

sys.stdout.write("\nCounts for Each Value of Categorical Label \n")
print (list(unique))
print (catCount)
