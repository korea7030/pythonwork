# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 12:02:33 2015

@author: Sang
"""

import requests
import json
from bs4 import BeautifulSoup


# 계정 정보를 가져오기 위한 url
base_html = 'http://www.kongregate.com/accounts/'

# kongregate 사이트의 user 정보 및 친구 정보를 가져오기 위한 url
# kongregate api 에서 복사한 url 임.
html = requests.get('http://api.kongregate.com/api/user_info.json?username=anotiks&friends=true')

# json 형태 이기 때문에 json load가 필요
js = json.loads(html.text)
# json 내용을 보면 friends 내용이 있음.
friends_list = js['friends']
# 친구목록 출력
print(friends_list)

for name in friends_list:  # 친구목록 수만큼 반복
    # 친구계정에 대한 정보 접근을 위한 url
    friend_html = base_html + name
    print(friend_html)

    # 친구 목록의 url get
    r = requests.get(friend_html)
    # 친구정보 값을 text로 변환
    friend_info_codes = r.text
    # beautifulsoup 으로 변환
    soup = BeautifulSoup(friend_info_codes)
    # point 정보 가져오기
    points = soup.find('span', class_='user_metric_stat').text
    print(points)
