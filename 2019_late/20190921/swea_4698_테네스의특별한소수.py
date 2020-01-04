import sys
sys.stdin = open('4698.txt')

def div(num):
    while num:
        c = num % 10
        if c == d:
            return False
        num = num // 10
    return True 

def table(n):
    t = [0,0] + [1]*(n-1)
    primes=[]
    for i in range(2,n+1):
        if t[i]:
            primes.append(i)
            for j in range(2*i, n+1, i):
                t[j] = 0
    return primes

# main
primes = table(1000000)

for t_case in range(int(input())):
    d, a, b = map(int, input().split())
    cnt = 0
    for i in range(len(primes)):
        if a <= primes[i] <= b:
            if not div(primes[i]):
                cnt += 1
        if primes[i] > b:
            break
    print('#{} {}'.format(t_case+1, cnt))

