# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 13:28:27 2016

@author: Administrator
한겨레 > 정치 (1~2 페이지)

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
    
base_url = 'http://www.hani.co.kr/'
board_url = 'http://www.hani.co.kr/arti/politics'
subject_path = './/h4[@class="article-title"]/a' ## 글 제목

with open('hani.csv', 'w', encoding = 'utf8') as f:
    w = csv.writer(f) ## csv 형식의 객체로 만들어줌
    for page in range(1,3):
        page_url = board_url+"/list"+str(page)+".html"
        print (page_url)
        for node in extract(page_url, subject_path):
            title = node.text_content()
            url = node.attrib['href']
            full_path = urljoin(base_url, url)
            print (full_path)
            post_content = extract(full_path, './/div[@class="article-text-font-size"]')[0]
            # print (post_content.text_content())
            w.writerow([title, full_path, post_content.text_content()])

