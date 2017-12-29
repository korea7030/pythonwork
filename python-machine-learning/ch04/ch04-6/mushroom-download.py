# -*- coding: utf-8 -*-
import urllib.request as req
local = "mushroom.csv"
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/mushroom/agaricus-lepiota.data"
req.urlretrieve(url, local)
print("ok")

"""
첫번째 열 : 독의 유무(독: p / 식용 : e)
두번째 열 : 버섯머리모양(벨 : b / 혹 : k / 오목 : s/ 평평한 : f)
네번째 열 : 머리색(갈색 : n / 황갈색 : b / 연한 갈색 : c/ 회색 : g/ 녹색 : r/분홍색 : p/보라색 : u/ 붉은색 : c / 흰색 : w/노란색 : y)
"""
