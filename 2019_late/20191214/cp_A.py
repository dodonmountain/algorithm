import sys;sys.stdin=open('cpa.txt')

T = int(input())

for tc in range(T):
    cnt = 0
    n = int(input())
    if n < 10:
        print(n)
    else:
        while n > 9:
            k = n % 10
            n //= 10
            cnt += 9
        if k:
            if n:
                cnt += n
            else:
                cnt += 1
        print(cnt)
        