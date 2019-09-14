import sys
sys.stdin = open('1979.txt')
from pprint import pprint

T= int(input())


for t_case in range(T):
    N, K = map(int, input().split())
    board = []
    res = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    tt = []
    rr = []
    for i in range(N):
        for j in range(N):
            tt.append(board[j][i])
        rr.append(tt)
        tt = []

    for i in board:
        tmp = []
        for j in range(N):
            if i[j] !=  0:
                tmp.append(i[j])
            else:
                if len(tmp) >= 2:
                    res.append(tmp)
                    tmp = []
                else:
                    tmp = []
        if len(tmp) >= 2:
            res.append(tmp)
    for i in rr:
        tmp = []
        for j in range(N):
            if i[j] !=  0:
                tmp.append(i[j])
            else:
                if len(tmp) >= 2:
                    res.append(tmp)
                    tmp = []
                else:
                    tmp = []
        if len(tmp) >= 2:
            res.append(tmp)
    cnt = 0
    for s in res:
        if len(s) == K:
            cnt += 1
    print("#{} {}".format(t_case+1, cnt))