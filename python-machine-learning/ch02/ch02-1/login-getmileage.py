# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# 아이디 / 비번
USER = "akachiki"
PASS = "akachiki10!"

# 세션 시작
session = requests.session()

# 로그인
login_info = {
    "m_id": USER,
    "m_passwd": PASS
}

url_login = "http://www.hanbit.co.kr/member/login_proc.php"
res = session.post(url_login, data=login_info)
res.raise_for_status()  # 오류 발생시 예외 처리

# 마이페이지 접근
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# 마일리지와 이코인 가져오기
soup = BeautifulSoup(res.text, "html.parser")
# print(soup)
mileage = soup.select_one(".mileage_section1 span").get_text()

ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지: " + mileage)
print("이코인: " + ecoin)
