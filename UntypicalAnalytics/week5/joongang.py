# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 11:49:14 2016

@author: Administrator
"""

import requests
import lxml.html
from urllib.parse import urljoin ## 상대주소 처리를 위한 모듈
import csv 

base_url = 'http://news.joins.com'
board_url = 'http://news.joins.com/politics?cloc=joongang|home|section2/' ## 게시판 url
subject_path = './/strong[@class="headline mg"]/a' ## 글 제목

with open('joongang.csv', 'w', encoding = 'utf8') as f:
    w = csv.writer(f) ## csv 형식의 객체로 만들어줌
    for node in extract(board_url, subject_path):
        title = node.text_content()
        url = node.attrib['href']
        full_path = urljoin(base_url, url)
        print (full_path)
        post_content = extract(full_path, './/div[@id="article_body"]')[0]
        # print (post_content.text_content())
        w.writerow([title, full_path, post_content.text_content()])

def extract(url, path):
    res = requests.get(url)
    res.encoding = 'utf8'
    root = lxml.html.fromstring(res.text)
    return root.xpath(path)