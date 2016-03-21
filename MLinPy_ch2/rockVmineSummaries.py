# -*- coding: utf-8 -*-
"""
Created on Wed Mar 16 14:54:40 2016

@author: Administrator

데이터 셋의 크기 측정 및 데이터 유형 확인
"""

# import urllib2
import urllib2
import sys

target_url = ("http://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib2.urlopen(target_url)

xList = []
labels = []

for line in data:
    row = line.strip().split(',')
    xList.append(row)
    

sys.stdout.write("Number of Rows of Data = "+str(len(xList))+'\n')
sys.stdout.write("Number of Columns of Data = "+str(len(xList[1]))+"\n")
nrow = len(xList)
ncol = len(xList[1])

print xList[1]
print ncol

type = [0]*3
colCounts = []

for col in range(ncol):
    for row in xList:
        try:
            a = float(row[col])
            if isinstance(a, float):
                type[0] += 1
        except ValueError:
            if len(row[col]) > 0:
                type[1] += 1
            else:
                type[2] += 1

    colCounts.append(type)
    type = [0]*3

sys.stdout.write("Col#" + '\t' + "Number" + '\t' +
                 "Strings" + '\t ' + "Other\n")
iCol = 0
for types in colCounts:
    sys.stdout.write(str(iCol) + '\t\t' + str(types[0]) + '\t\t' +
                     str(types[1]) + '\t\t' + str(types[2]) + "\n")
    iCol += 1