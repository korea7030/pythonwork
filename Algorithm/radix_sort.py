# -*- config: utf-8 -*-


def radix_sort(arr, base):
    size = len(arr)
    max_val = max(arr)  # 최대값
    exp = 1  # 자리수

    output = [0] * size
    while exp <= max_val:
        count = [0] * base

        for i in range(size):
            print((arr[i] // exp) % base)
            count[(arr[i] // exp) % base] += 1

        print('first count : ' + str(count))

        for i in range(1, base):
            count[i] += count[i-1]

        print('cumsum second count : ' + str(count))

        for i in range(size-1, -1, -1):
            j = (arr[i] // exp) % base
            output[count[j] - 1] = arr[i]
            count[j] -= 1

        print('output : ' + str(output))

        for i in range(size):
            arr[i] = output[i]
        exp *= base

    return output


if __name__ == '__main__':
    arr = [359, 654, 430, 220, 219, 543, 756, 800]
    result = radix_sort(arr, 10)
    print(result)