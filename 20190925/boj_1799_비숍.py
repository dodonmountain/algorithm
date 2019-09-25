import sys;sys.stdin = open('1799.txt')
from pprint import pprint
N = int(input())
board = [list(map(int, input().split())) for _  in range(N)]
for p in range(N):
    for i in range(N):
        if board[p][i] == 1:
            dr = 1
            while True:
                if p + dr <= N - 1 and i + dr <= N - 1:
                    board[p+dr][i+dr] = 0
                else:break
                dr += 1
            dl = 1
            while True:
                if p + dl <= N - 1  and i - dl >= 0:
                    board[p+dl][i-dl] = 0
                else:break
                dl += 1
            board[p][i] = 2
res = 0
for i in range(N):
    res += board[i].count(2)
print(res)