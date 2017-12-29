# -*- coding: utf-8 -*-
import urllib.request as req
import os.path
import random
import json

# JSON 데이터 내려 받기
url = 'http://api.github.com/repositories'
savename = "repo.json"
if not os.path.exists(url):
    req.urlretrieve(url, savename)

# JSON 파일 분석
items = json.load(open(savename, "r", encoding="utf-8"))

# 출력
for item in iems:
    print(item["name"] + " - " + item["owner"]["login"])
