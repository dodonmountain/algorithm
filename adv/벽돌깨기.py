
from pprint import pprint
import sys
sys.stdin = open('brick.txt')

from copy import deepcopy
from collections import deque
def find_top(board):
    tops = []
    for i in range(W):
        for j in range(H):
            if board[j][i] != 0:
                tops.append((i, j))
                break
    return tops


def explode(position, board):
    q = deque()
    q.append(position)
    while q:
        x, y = q.popleft()
        power = board[x][y]
        for i in range(1, power):
            if 0 < x + i < H-1:
                if board[x+i][y] > 1:
                    q.append((x+i, y))
                board[x+i][y] = 0
            if 0 < x - i < H-1:
                if board[x-i][y] > 1:
                    q.append((x-i, y))
                board[x-i][y] = 0
            if 0 < y+i < W-1:
                if board[x][y+i] > 1:
                    q.append((x, y+i))
                board[x][y+i] = 0
            if 0 < y-i < W-1:
                if board[x][y-i] > 1:
                    q.append((x, y-i))
                board[x][y-i] = 0
    return fall(board)


def fall(board):
    rt = rotate(board)
    for i in range(W):
        for j in range(H-1,-1,-1):
            if rt[i][j] == 0:
                rt[i].append(rt[i].pop(j))
    rot = []
    for i in range(W-1, -1, -1):
        tmp = []
        for j in range(H):
            tmp.append(board[j][i])
        rot.append(tmp)
    return rot

def rotate(board):
    copy = [[0] * H for _ in range(W)]
    for i in range(H):
        for j in range(W):
            copy[j][W-1-i] = board[i][j]
    return copy

def solve(depth, board):
    global answer
    if depth == N:
        cnt = 0
        for i in range(H):
            for j in range(W):
                if board[i][j] != 0:
                    cnt += 1
                    if cnt > answer:
                        return
        if cnt < answer:
            answer = cnt
        return
    tops = find_top(board)
    for tries in tops:
        x, y = tries
        solve(depth+1, explode((x, y), board))


T = int(input())

for tc in range(T):
    N, W, H = map(int, input().split())
    original_board = [list(map(int, input().split())) for _ in range(H)]
    board = deepcopy(original_board)
    answer = 0x9999999
    solve(0, board)
