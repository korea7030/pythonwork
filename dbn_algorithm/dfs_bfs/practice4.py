# -*- coding: utf-8 -*-
"""
미로 탈출(p. 152)
 - 1로 되어있는 길로만 간다
 - 방문한 거리는 1 이외의 다른 숫자로 표시
"""
from collections import deque

# input N, M
n, m = map(int, input().split())

# 2차원 배열
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 네 방향(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 현재 방향에서 네방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            # 괴물 무시
            if graph[nx][ny] == 0:
                continue

            # 노드를 처음방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))

    return graph[n-1][m-1]


print(bfs(0,0))
