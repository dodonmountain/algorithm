import sys
sys.stdin = open('1244.txt')

def swop(a,b):
    arr[a], arr[b] = arr[b], arr[a]
    return

def made(arr):
    res = 0
    for i in range(L-1,-1,-1):
        res += arr[i] * (10**(L-i-1))
    return res

def solve(s):
    global answer
    if s == b:
        tmp = made(arr) 
        if tmp > answer:
            answer = tmp
        return
    for i in range(L):
        for j in range(L):
            if i < j:
                swop(i, j)
                solve(s + 1)
                swop(i, j)


for t_case in range(int(input())):
    a, b = map(int, input().split())
<<<<<<< HEAD
    if b > len(str(a)) // 2:
        b = b // 2 + 1
=======
>>>>>>> 110fb913b2743d48acfde5a7fd1ffece3f313f23
    arr = list(map(int, list(str(a))))
    if b > len(arr) >> 1:
        b = (b >> 1) + 1 
    L = len(arr)
    answer = 0
    solve(0)
    print('#{} {}'.format(t_case+1, answer))
