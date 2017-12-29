# -*- coding: utf-8 -*-
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot
import pandas as pd

# 키와 몸무게 데이터 읽기
tbl = pd.read_csv("bmi.csv")

# 컬럼명을 거르고 정규화
label = tbl["label"]
w = tbl["weight"] / 100  # 최대 100 kg 이라 가정
h = tbl["height"] / 200  # 최대 200cm 이라 가정

wh = pd.concat([w, h], axis=1)  # 열

# 학습전용 데이터와 테스트 데이터 분류
data_train, data_test, label_train, label_test = train_test_split(wh, label)

# 데이터 학습
clf = svm.SVC()
clf.fit(data_train, label_train)

# 데이터 예측
pred = clf.predict(data_test)

# 결과 테스트
ac_score = metrics.accuracy_score(label_test, pred)
cl_report = metrics.classification_report(label_test, pred)
print('정답률 : ', ac_score)
print("리포트 : ", cl_report)

# precision : True로 예측한 것 중에 실제 True인 것의 비율
# recall : 실제 True인 것 중에 True로 예측한 것의 비율
