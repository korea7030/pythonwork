# -*- coding: utf-8 -*-
'''
1~N 까지의 합을 분할정복 합으로 표현
 : 분할정렬을 기초로 하여 분할할 수 없는 개수까지 분할 후 각가의 합계의 병합된 값을 구하는 것
 계산과정
  : (1+2+...+N/2)+((N/2+1)+(N/2+2)+(N/2+3)+(N/2+4)+(N/2+5)+...+(N/2+N/2))
  : (1+2+...+N/2)+(N/2+N/2+N/2+N/2)+(1+2+3+...+N/2)
  : (2*(1+2+...+N/2))*((N/2)*(N/2))
'''


def divide_merge_sum(n: int):
    if n == 1:
        return 1
    if n % 2 == 1:
        return n + divide_merge_sum(n - 1)

    return (2 * divide_merge_sum(n / 2)) + ((n / 2) * (n / 2))


'''
1~N 까지의 합을 재귀함수로 구현
'''


def sum(n: int):
    if n == 1:
        return 1
    else:
        return n + sum(n - 1)


if __name__ == "__main__":
    print(divide_merge_sum(100))
    print(sum(100))
