# -*- coding: utf-8 -*-
import codecs
import os

filename = 'list-euckr.csv'
# Atom 에서 실행 시
# csv = codecs.open(os.getcwd()+"\\python-machine-learning\\ch03\\ch03-1\\"+filename, "r", "euc-kr").read()
csv = codecs.open(filename, "r", "euc-kr").read()
# CSV을 파이썬 리스트로 변환
data = []
rows = csv.split("\r\n")

for row in rows:
    if row == "": continue

    cells = row.split(",")
    data.append(cells)

# 결과 출력
for c in data:
    print(c[1], c[2])
