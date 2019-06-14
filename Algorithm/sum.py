def sumN(n):
    res = 0
    for i in range(n+1):
        res += i
    return res

def sumN2(n):
    return int((n+1)*n/2)

def sumN3(n):
    if n % 2 == 0:
        return int((n+1)*n/2)
    else:
        return int(n*(n-1)/2 + n)
    
def sumN4(n):
    if n % 2 == 0:
        return int((n+1)*n/2)
    else:
        return int(sumN4(n-1)+n)

if __name__=='__main__':
    print(sumN(10))
    print(sumN2(10))
    print(sumN3(11))
    print(sumN4(11))
