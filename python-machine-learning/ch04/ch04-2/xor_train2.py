# -*- coding: utf-8 -*-
import pandas as pd
from sklearn import svm, metrics
# 프레임워크 사용하여 xor_train.py 와 비교

# XOR 계산 결과 데이터
xor_input = [
    #P, Q, result
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]

# 입력을 위한 학습 데이터와 테스트 데이터 분리
xor_df = pd.DataFrame(xor_input)
xor_data = xor_df.ix[:, 0:1]  # 데이터
xor_label = xor_df.ix[:, 2]

# 학습결과 예측
clf = svm.SVC()
clf.fit(xor_data, xor_label)
pre = clf.predict(xor_data)

# 정답률
ac_score = metrics.accuracy_score(xor_label, pre)
print("정답률 : ", ac_score)
