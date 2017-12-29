# -*- coding: utf-8 -*-
from selenium import webdriver
USER = "korea7030"
PASS = "wogusdlRj1!"

# phantomjs 드라이버 호출
browser = webdriver.PhantomJS("C://phantomjs-2.1.1-windows//bin//phantomjs.exe")
browser.implicitly_wait(3)

# 로그인 페이지 접근
url_login = "https://nid.naver.com/nidlogin.login"
browser.get(url_login)
print('로그인 페이지 접근')

# 텍스트 박스에 아이디와 비번 입력
e = browser.find_element_by_id("id")
e.clear()
e.send_keys(USER)
e = browser.find_element_by_id("pw")
e.clear()
e.send_keys(PASS)

# 입력 양식 전송해서 로그인
form = browser.find_element_by_css_selector("input.btn_global[type=submit]")
form.submit()
print("로그인 버튼을 클릭")

# 쇼핑 페이지의 데이터 가져오기
browser.get("https://order.pay.naver.com/home?tabMenu=SHOPPING")

# 쇼핑 목록 출력
products = browser.find_elements_by_css_selector(".p_info span")
print(products)

for product in products:
    print("-", product.text)
