# -*- coding: utf-8 -*-
def calc_distance(a, b):
    '''레벤슈타인 거리 계산하기
        : 단어 A와 B가 얼마나 유사한지를 측정하기 위해 A를 B로 바꾸기 위해 문자열을 어떻게 수정해 나가야 하는지 규정하고 그 수정횟수를 두 단어 사이의 거리라고 칭함
    '''

    if a == b:
        return 0
    a_len = len(a)
    b_len = len(b)
    if a == "":
        return b_len
    if b == "":
        return a_len

    # 2차원 표(a_len+1, b_len+1) 준비하기
    matrix = [[] for i in range(a_len + 1)]

    for i in range(a_len + 1):
        matrix[i] = [i for j in range(b_len + 1)]
    # 0일때 초기값 설정
    for i in range(a_len + 1):
        matrix[i][0] = i

    for j in range(b_len + 1):
        matrix[0][j] = j

    # 표 채우기
    for i in range(1, a_len + 1):
        ac = a[i - 1]
        for j in range(1, b_len + 1):
            bc = b[j - 1]
            cost = 0 if (ac == bc) else 1

            matrix[i][j] = min([matrix[i - 1][j] + 1,  # 문자 삽입
                                matrix[i][j - 1] + 1,  # 문자 제거
                                matrix[i - 1][j - 1] + cost  # 문자변경
                                ])

    return matrix[a_len][b_len]


print(calc_distance("가나다라", "가마바라"))

# 실행 예
samples = ["신촌역", "신천군", "신천역", "신발", "마곡역"]
base = samples[0]
r = sorted(samples, key=lambda n: calc_distance(base, n))

for n in r:
    print(calc_distance(base, n), n)
