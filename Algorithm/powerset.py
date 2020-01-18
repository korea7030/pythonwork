# -*- codingL utf-8 -*-
# 멱집합

data = ['a', 'b', 'c', 'd', 'e', 'f']
n = len(data)
boolean_p = [False] * (n+1)


def powerset(k):
    if k == n:
        for i in range(0, n):
            if boolean_p[i]:
                print(data[i] + " ")
        print()
        return

    # tree 의 왼쪽
    boolean_p[k] = False
    powerset(k+1)
    # tree 의 오른쪽
    boolean_p[k] = True
    powerset(k+1)


if __name__ == '__main__':
    powerset(0)