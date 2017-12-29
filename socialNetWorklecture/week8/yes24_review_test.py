# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 08:57:23 2015

@author: Sang
"""

#import requests
from bs4 import BeautifulSoup
import codecs
from selenium import webdriver


f_sele = codecs.open('gmarket_review_sele.txt', encoding='utf-8', mode='w')
url = 'http://item2.gmarket.co.kr/Item/detailview/Item.aspx?goodscode=119577841'


driver = webdriver.Firefox()

driver.get(url)
driver.implicitly_wait(10)

element = driver.find_element_by_id('aGoodsAnalysis')
jcode = element.get_attribute("onclick")
driver.execute_script(jcode)
driver.implicitly_wait(10)
html = driver.page_source

f_sele.write(html)

driver.close()
f_sele.close()
# r=requests.get(url)
# f_save.write(r.text)
# f_save.close()
