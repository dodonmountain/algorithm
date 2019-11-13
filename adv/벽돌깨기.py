import sys;sys.stdin = open('brick.txt')
from pprint import pprint


def find_top():
    tops = []
    for i in range(W):
        for j in range(H):
            if board[j][i] != 0:
                tops.append((i,j))
                break
    return tops

def anti_clock_rotate():
    tmp = [[0]*W for _ in range(H)]
    for i in range(W):
        for j in range(H):
            tmp[j][i] = board[i][j]
    return tmp

def clock_rotate():
    tmp = [[0]*W for _ in range(H)]
    for i in range(W-1,-1,-1):
        for j in range(H-1,-1,-1):
            tmp[j][i] = board[i][j]
    return tmp

def explode():
    pass

T = int(input())
T = 1
for tc in range(T):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    pprint(board, width=W*10)
    pprint(anti_clock_rotate(),width=W*10)
    pprint(clock_rotate(),width=W*10)