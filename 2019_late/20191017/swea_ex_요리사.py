import sys;sys.stdin = open('input.txt')

from itertools import combinations as cb

for t_case in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    minnow = 999999
    cand = (list(cb(range(N),N//2)))
    for i in range(len(cand)):
        s = cand[i]
        s2 = cand[-i-1]
        A, B = 0, 0
        for w in s:
            for e in s:
                A += board[w][e]
        for i in s2:
            for j in s2:
                B += board[i][j]
        tmp = abs(A-B)
        if tmp < minnow:
            minnow = tmp
    print('#{} {}'.format(t_case+1, minnow))
