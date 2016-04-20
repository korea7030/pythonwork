# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 14:23:34 2016

@author: Administrator

조선일보 뉴스 > 정치 > 국회,정당(1~2페이지)

"""

import requests
import lxml.html
from urllib.parse import urljoin ## 상대주소 처리를 위한 모듈
import csv 

def extract(url, path):
    res = requests.get(url)
    print (res.encoding)
    res.encoding = 'cp949'
    root = lxml.html.fromstring(res.text)
    # print(root.xpath(path).text_content())
    return root.xpath(path)

best_url = 'http://news.chosun.com/politics/index.html'
board_url = 'http://news.chosun.com/svc/list_in/list.html?catid=21' # 조선일보 뉴스 - 정치
subject_path = './/dt/a'

with open('chosun.csv', 'w', encoding = 'utf8') as f:
    w = csv.writer(f) ## csv 형식의 객체로 만들어줌
    for page in range(1,3):
        page_url = board_url+'&pn={}'.format(page)
        for node in extract(page_url, subject_path):
            title = node.text_content()
            url = node.attrib['href']

            post_content = extract(url, './/div[@class="par"]')[0]
            print (post_content.text_content())
            w.writerow([title, url, post_content.text_content()])            

