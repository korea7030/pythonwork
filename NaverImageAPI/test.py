# -*- coding: utf-8 -*-
"""
Created on Fri May 20 22:09:31 2016

@author: Administrator
"""
import requests
import lxml.html
import csv

url = 'http://www.inven.co.kr/board/powerbbs.php?come_idx=2736&query=list&my=&category=&sort=PID&orderby=&name=&subject=&content=&keyword=&sterm=&eq=&iskin=&mskin=&p=1'

with open('inven.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f)
    for i in range(1, 2):
        res = requests.get(url.format(i))  # 기사 목록
        element = lxml.html.fromstring(res.text)
        for news_link in element.xpath('.//a[@class="sj_ln"]'):
            try:
                res = requests.get(news_link.attrib['href'])  # 인벤 뉴스 링크
                # print(news_link.attrib['href'])
                news = lxml.html.fromstring(res.text)
                # print (news[1].text_content())
                body = news.xpath('.//div[@class="articleContent"]')[0]
                print(body.text_content())
                writer.writerow([body.text_content()])
            except:
                continue
