# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 00:07:30 2016

@author: Administrator
"""

import requests
import lxml.html
from urllib.parse import urljoin ## 상대주소 처리를 위한 모듈
import csv 

best_url = 'http://www.bobaedream.co.kr/list?code=best'
board_url = 'http://www.bobaedream.co.kr/list?code=best&or_gu=10&or_se=desc&pagescale=30&type=list'
subject_path = './/a[@class="bsubject"]'

with open('bobae.csv', 'w', encoding = 'utf8') as f:
    w = csv.writer(f) ## csv 형식의 객체로 만들어줌
    for page in range(1,3):
        page_url = board_url+'&page={}'.format(page)
        for node in extract(page_url, subject_path):
            title = node.text_content()
            url = node.attrib['href']
            full_path = urljoin(best_url, url)
            # print (full_path)
            post_content = extract(full_path, './/div[@class="content02"]/div/p')
            print (post_content)
            # post_content2 = extract(full_path, './/div[@class="bodyCont"]')
            # post_content = extract_getattribute(full_path, './/div[@class="bodyCont"]')     
            # try :
            #    w.writerow([title, full_path, post_content.text_content()])
            #except :
            #    print ("error 발생")
            # print (post_content[0].text_content())
            

def extract(url, path):
    res = requests.get(url)
    res.encoding = 'utf8'
    root = lxml.html.fromstring(res.text)
    print(root.xpath(path).text_content())
    return root.xpath(path)

def extract_getattribute(url, path):
    res = requests.get(url)
    res.encoding = 'utf8'
    root = lxml.html.fromstring(res.text)
    return root.xpath(path)