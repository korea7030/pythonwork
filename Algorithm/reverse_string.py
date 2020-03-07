def reverse_string_using_for(string):
    result = ''
    for i in range(len(string)-1, -1, -1):
        result += string[i]
    return result


def reverse_string_using_while(string):
    cnt = len(string)
    result = ''
    while cnt>0:
        cnt -= 1
        result += string[cnt]
    return result


def reverse_string_using_slicing(string):
    return string[::-1]


def reverse_string_using_reversed(string):
    result = ''
    for i in reversed(string):
        result += i

    return result


res1 = reverse_string_using_for('abcde')
print(res1)
res2 = reverse_string_using_for('abcde')
print(res2)
res3 = reverse_string_using_while('abcde')
print(res3)
res4 = reverse_string_using_reversed('abcde')
print(res4)