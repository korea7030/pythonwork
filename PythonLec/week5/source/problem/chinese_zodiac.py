# coding: UTF-8
# Chinese Zodiac

# input 함수로 받은 데이터의 타입 = 문자열
# int: integer로 변환해주는 변환 함수
year = int(input("Enter a year: "))

if year % 12 == 8:
	animal = "용"
elif year % 12 == 9:
	animal = "뱀"
elif year % 12 == 10:
	animal = "말"
elif year % 12 == 11:
	animal = "양"
elif year % 12 == 0:
	animal = "원숭이"
elif year % 12 == 1:
	animal = "닭"
elif year % 12 == 2:
	animal = "개"
elif year % 12 == 3:
	animal = "돼지"
elif year % 12 == 4:
	animal = "쥐"
elif year % 12 == 5:
	animal = "소"
elif year % 12 == 6:
	animal = "호랑이"
elif year % 12 == 7:
	animal = "토끼"

# 출력해보세n요.
#n 쥐 띠입니다
print(animal)

print(animal + "띠입니다.")
