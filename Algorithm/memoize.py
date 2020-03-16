memo = {1:1, 2:1}


def fibonacci(n):
    if n == 0:
        return 0

    if n not in memo:
        print('n-1 : {}, n-2 : {}'.format(n-1, n-2))
        memo[n] = fibonacci(n-1) + fibonacci(n-2)

    print('memo n : {}, memo[n] : {}'.format(n, memo[n]))
    return memo[n]


def fibonacci2(n):
    if n == 1:
        return 1
    if n == 2:
        return 1

    return fibonacci2(n-1) + fibonacci2(n-2)


res = fibonacci(20)
print(res)

res2 = fibonacci2(20)
print(res2)