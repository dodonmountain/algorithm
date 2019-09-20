import sys
sys.stdin = open('1244.txt')

def swop(a,b):
    arr[a], arr[b] = arr[b], arr[a]
    return

def made(a):
    res = 0
    rev = arr[::-1]
    for i in range(L):
        res += rev[i] * 10**i
    return res

def solve(s):
    global call
    if s == b:
        if made(arr) > call:
            call = made(arr)
        return
    for i in range(L):
        for j in range(L):
            if i < j:
                swop(i, j)
                solve(s+1)
                swop(i, j)

T = int(input())

for t_case in range(T):
    a, b = map(int, input().split())
    if b > 2:
        b = b // 2 + 1
    arr = list(map(int, list(str(a))))
    L = len(arr)
    call = 0
    used = [0] * L
    solve(0)
    print('#{} {}'.format(t_case+1, call))
