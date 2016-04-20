# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:10:38 2016

@author: Administrator
MLBPARK > 뉴스 > 프로야구 (페이지 1~2)
"""

import requests
import lxml.html
from urllib.parse import urljoin ## 상대주소 처리를 위한 모듈
import csv 

def extract(url, path):
    res = requests.get(url)
    res.encoding = 'utf8'
    root = lxml.html.fromstring(res.text)
    return root.xpath(path)

base_url = 'http://mlbpark.donga.com/mlbpark/newsfeed.php?source=101&m=newsfeed'
board_url = 'http://mlbpark.donga.com/mlbpark/newsfeed.php?p={}&m=newsfeed&source=101&b=newsfeed' ## 게시판 url
subject_path = './/div[@class="title"]/a' ## 글 제목

with open('mlbpark.csv', 'w', encoding = 'utf8') as f:
    w = csv.writer(f) ## csv 형식의 객체로 만들어줌
    for page in range(1,91,30):
        page_url = board_url.format(page)
        for node in extract(page_url, subject_path):
            title = node.text_content()
            url = node.attrib['href']
            full_path = urljoin(base_url, url)
            print (full_path)
            post_content = extract(full_path, './/div[@id="contentDetail"]')[0]
            # print (post_content.text_content())
            w.writerow([title, full_path, post_content.text_content()])

