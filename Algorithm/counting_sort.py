def counting_sorted(arr, K):
    # 각 요소가 몇개씩 들어가는지를 담을 c배열을 k 크기로 초기화
    c = [0] * K
    sorted_arr = [0] * len(arr)

    # 입력된 arr의 각 요소들을 세아려 c에 기록
    for i in arr:
        print("i : "+str(i))
        c[i] += 1

    print('c array : '+str(c))
    # c는 기록된 이전 요소들의 누적 합으로 할당
    for i in range(1, K):
        c[i] += c[i-1]

    print('cumsum c array : '+str(c))
    # c값을 기준으로 재배치
    for i in arr:
        sorted_arr[c[i]-1] = i
        c[i] -= 1

    return sorted_arr


arr = [3, 5, 1, 2, 9, 6, 4, 7, 5]
print(counting_sorted(arr, 10))