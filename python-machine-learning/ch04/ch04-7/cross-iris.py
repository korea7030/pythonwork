# -*- coding: utf-8 -*-
from sklearn import svm, metrics
import random
import re

# 붓꽃 csv 파일
lines = open("iris.csv", "r", encoding="utf-8").read().split("\n")


def f_tonum(n): return float(n) if re.match(r'^[0-9\.]+$', n) else n


def f_cols(li): return list(map(f_tonum, li.strip().split(',')))


csv = list(map(f_cols, lines))
del csv[0]  # 헤더 제거

random.shuffle(csv)

# 데이터를 K 개로 분할
K = 5
csvk = [[] for i in range(K)]

# print("csvk : ", csvk)

for i in range(len(csv)):
    print("csv : ", i + 1, csv[i])
    csvk[i % K].append(csv[i])  # 5개씩 하나의 리스트

# print("csvk : ", csvk)

# 리스트를 훈련 데이터와 테스트 데이터 분류 함수


def split_data_label(rows):
    data = []
    label = []
    for row in rows:
        data.append(row[0:4])
        label.append(row[4])

    return (data, label)

# 정답률 구하기


def calc_score(test, train):
    test_f, test_l = split_data_label(test)
    train_f, train_l = split_data_label(train)

    # 학습 시키고 정답률
    clf = svm.SVC()
    clf.fit(train_f, train_l)
    pre = clf.predict(test_f)
    return metrics.accuracy_score(test_l, pre)


# K 개로 분할해서 정답 구하기
score_list = []
for testc in csvk:
    # testc 이외의 데이터를 훈련전용 데이터로 사용
    trainc = []
    for i in csvk:
        if i != testc:
            trainc += i
    sc = calc_score(testc, trainc)
    score_list.append(sc)

print("각각의 정답률 = ", score_list)
print("평균 정답률 = ", sum(score_list) / len(score_list))
