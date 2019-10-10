import sys;sys.stdin=open('1233.txt')

def trav(v):
    if v == 0:return
    trav(L[v])
    trav(R[v])


for t_case in range(10):
    N = int(input())
    O, L, R = [0] * (N+1), [0] * (N+1), [0] * (N+1)
    for i in range(N):
        arr = list(input().split())
        if len(arr) == 4:
            p, o, l, r = int(arr[0]), arr[1], int(arr[2]), int(arr[3])
        elif len(arr) == 3:
            p, o, l, r = int(arr[0]), arr[1], int(arr[2]), 0
        elif len(arr) == 2:
            p, o, l, r = int(arr[0]), arr[1], 0, 0
        L[p], R[p] = l, r
        O[p] = o
    flag = 1
    trav(1)
    print('#{} {}'.format(t_case+1, int(flag)))