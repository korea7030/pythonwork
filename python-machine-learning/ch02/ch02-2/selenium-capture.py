# -*- coding: utf-8 -*-
from selenium import webdriver

url = "http://www.naver.com/"
# phantomJS 드라이버 추출

browser = webdriver.PhantomJS("C://phantomjs-2.1.1-windows//bin//phantomjs.exe") ## phantomjs 파일 경로 필요

# 3초 대기
browser.implicitly_wait(3)

# URL 읽기
browser.get(url)

# 화면캡쳐 저장
browser.save_screenshot("Website.png")

browser.quit()
