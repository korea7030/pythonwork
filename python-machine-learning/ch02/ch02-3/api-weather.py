# -*- coding: utf-8 -*-
import requests
import json

# API 키를 지정.
apikey = "6b46865b80b9c12ecbda4051286b94c0"

# 날씨 확인할 도시 지정
cites = ["Seoul,KR", "Tokyo,JP", "New York,US"]

# API 지정
api = "http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}"

# 캘빈 온도는 섭씨 온도로 변환
k2c = lambda k: k-273.15

# 각 도시의 정보 추출
for name in cites:
    url = api.format(city=name, key=apikey)

    # API에 요청 보내기
    r = requests.get(url)

    # 결과 반환
    data = json.loads(r.text)
    print(data)
    # 결과 출력
    print("+ 도시 =", data["name"])
    print("| 날씨 =", data["weather"][0]["description"])
    print("| 최저 기온 =", k2c(data["main"]["temp_min"]))
    print("| 최고 기온 =", k2c(data["main"]["temp_max"]))
    print("| 습도 =", data["main"]["humidity"])
    print("| 기압 =", data["main"]["pressure"])
    print("| 풍향 =", data["wind"]["deg"])
    print("| 풍속 =", data["wind"]["speed"])
    print("")
