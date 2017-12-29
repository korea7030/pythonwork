# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 10:59:10 2015

@author: Administrator
"""

from bs4 import BeautifulSoup
import codecs
from selenium import webdriver
import requests

##################### yes24의 회원리뷰 보기#######################
url = 'http://www.yes24.com/24/goods/15058512'

r = requests.get(url)

# firefox 창을 띄운다.
driver = webdriver.Firefox()

# 해당 url 을 통해 사이트 접속
driver.get(url)
driver.implicitly_wait(10)

# 회원리뷰 버튼 클릭
element = driver.find_element_by_xpath(
    '/html/body/div[2]/div[5]/form/table/tbody/tr/td/div/ul/li[7]/a/img')
element.click()

# 전체리뷰 펼쳐보기 클릭
element2 = driver.find_element_by_xpath(
    '/html/body/div[2]/div[5]/form/table/tbody/tr/td/div/div[8]/div[12]/div[3]/div[1]/span/a/img[2]')
element2.click()

html = driver.page_source

## 이후는 soup으로 저번에 배운것과 같이 보고싶은 내용만 뽑아서 사용 가능 ###
soup = BeautifulSoup(html)
print(soup.find_all('span', class_='reviewContent FullContent'))

driver.close()
#################################################################

######################## G마켓의 상품분석평 보기 ################
# a tag의 onclick(java script 내용 수행)
f_sele = codecs.open('gmarket_review_sele.txt', encoding='utf-8', mode='w')
url = 'http://item2.gmarket.co.kr/Item/detailview/Item.aspx?goodscode=119577841'

# firefox 창을 띄운다.
driver = webdriver.Firefox()

# url을 통해 해당 사이트 접속
driver.get(url)
driver.implicitly_wait(10)

# 상품분석평 보기의 id 값
element3 = driver.find_element_by_id('aGoodsAnalysis')
# id에 대한 javascript 수행을 위한 onclick 속성 가져오기
jcode = element3.get_attribute("onclick")
# 해당 onclick에 있는 javascript 수행
driver.execute_script(jcode)
driver.implicitly_wait(10)
html = driver.page_source

f_sele.write(html)

driver.close()
f_sele.close()

##################################################################
