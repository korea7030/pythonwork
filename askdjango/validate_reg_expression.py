import re

val = "01012341234abc"
# 정규 표현식 쓸 때 r을 써줘야 함.(raw를 의미)
pattern = r"^01[016789][1-9]\\d{6,7}$" # raw

if re.match(pattern, val):
    print("matched")
else:
    print("invalid")
