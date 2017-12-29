# -*- coding: utf-8 -*-
import csv
import codecs

# CSV 파일 열기
filename = "list-euckr.csv"
fp = codecs.open(filename, "r", "shift_jis", "euc-kr")

# 한줄씩 읽기
reader = csv.reader(fp, delimiter=",", quotechar='"')
for cells in reader:
    print(cells[1], cells[2])
