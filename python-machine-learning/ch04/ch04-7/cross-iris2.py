# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import svm, metrics, model_selection
import random, re

csv = pd.read_csv("iris.csv")

# 데이터 분할
data = csv[["SepalLength", "SepalWidth", "PetalLength", "PetalWidth"]]
label = csv["Name"]

# 크로스 벨리데이션
clf =svm.SVC()
scores = model_selection.cross_val_score(clf, data, label, cv=5)
print("각각의 정답률 = ", scores)
print("평균 정답률 = ", scores.mean())
