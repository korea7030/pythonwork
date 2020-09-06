# -*- coding: utf-8 -*-
"""
음료수 얼려 먹기(p.149)
 - 상하좌우 표시
"""
n, m = map(int, input().split())

# 2차원 배열
graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        # 방문 표시
        graph[x][y] = 1

        # 상하좌우 재귀호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
