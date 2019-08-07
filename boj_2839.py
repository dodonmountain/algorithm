N = int(input())
dibi = N // 5
N %= 5
res = 0
while dibi > -1:
    if N % 3 == 0:
        res = N // 3
        N = N % 3
        break
    
    dibi -= 1
    N += 5
print((N==0) and (res+dibi) or -1)