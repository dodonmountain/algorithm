import functools 

def solution(numbers):
    memo = [0] * len(numbers)
    def comp(a,b):
        if int(str(a) + str(b)) > int(str(b) + str(a)):
            return -1
        elif int(str(a) + str(b)) < int(str(b) + str(a)):
            return 1
        else:
            return 0
    cmp = functools.cmp_to_key(comp)
    numbers.sort(key=cmp)
    res = ''
    for i in numbers:
        res += str(i)
    return str(int(res))