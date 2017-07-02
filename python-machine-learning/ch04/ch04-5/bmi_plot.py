# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

# csv 파일 불러오기
tbl = pd.read_csv("bmi.csv", index_col=2)

# 그래프 그리기
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

# 서브 플롯 전용 - 레이블을 임의의 색으로 칠함
def scatter(lbl, color):
    b = tbl.loc[lbl]
    ax.scatter(b["weight"], b["height"], c=color, label=lbl)

scatter("fat", "red")
scatter("normal", "yellow")
scatter("thin", "purple")

ax.legend()
plt.savefig("bmi-test.png")
