# -*- coding: utf-8 -*-
"""
무지의 먹랑 라이브(p. 316)
"""
from queue import PriorityQueue


def solution(food_times, k):
    # 섭취해야할 음식이 없다면 -1
    if sum(food_times) <= k:
        return -1

    q = PriorityQueue()
    for i in range(len(food_times)):
        q.put((food_times[i], i+1)) # (food_times, index)

    sum_value = 0  # 누적되는 k에서 빠지는 값
    previous = 0  # 이전에 다 먹은 음식 값
    length = len(food_times)  # 전체 음식 개수

    # 현재 상황에서 다 먹어서 뺄 수 있는지 k와 비교
    # sum_value - (빼버릴 임식 시간 - 이전 음식 값) * 현재 음식 개수
    while sum_value + ((q.queue[0][0] - previous) * length) <= k:
        now = q.get()[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now

    result = sorted(q.queue, key=lambda x: x[1])
    # 최종적으로 남은 음식 중에서 현재 k가 몇 번째 음식인지 확인, (k- sum_value) % length
    return result[(k - sum_value) % len(q.queue)][1]

