memo = {1:1, 2:1}

def fibonacci2(n):
    if n==0:
        return 0
    elif n not in memo:
        memo[n] = fibonacci2(n-1) + fibonacci2(n-2)
    
    return memo[n]

def fibonacci(n):
    a,b = 1,0
    for i in range(n):
        a,b = b, a+b
        
    return b
    
if __name__=='__main__':
    count = int(input())

    for i in range(count):
        n = int(input())
        print(str(fibonacci2(n-1)) + ' ' + str(fibonacci2(n)))
        print(str(fibonacci(n-1)) + ' ' + str(fibonacci(n)))