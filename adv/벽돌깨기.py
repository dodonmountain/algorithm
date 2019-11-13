from pprint import pprint
import sys
sys.stdin = open('brick.txt')

from copy import deepcopy
from collections import deque

def find_top(bd):
    tops = []
    for i in range(W):
        for j in range(H):
            if bd[j][i]:
                tops.append((j,i))
                break
    return tops

def solve(d, top, brd, cnt):
    global answer
    if answer == 0:return
    if cnt == 0:return
    board = deepcopy(brd)
    q = deque()
    q.append(top)
    while q:
        x, y = q.popleft()
        power = board[x][y]
        if board[x][y]:
            board[x][y], cnt = 0, cnt - 1
        for i in range(power):
            if x + i < H and board[x+i][y]:q.append((x+i, y))
            if -1 < x-i and board[x-i][y]:q.append((x-i, y))
            if y+i < W and board[x][y+i]:q.append((x, y+i))
            if -1 < y-i and board[x][y-i]:q.append((x, y-i))
    for i in range(W):
        tmp = []
        for j in range(H):
            if board[j][i]:
                tmp.append(brd[j][i])
        tmp = ([0] * (H - len(tmp))) + tmp
        for j in range(H):
            board[j][i] = tmp[j]
    if d == N:
        answer = min(cnt, answer)
        return
    if cnt:
        tops = find_top(board)
        for top in tops:
            solve(d + 1, top, board, cnt)
    else:
        answer = 0
        return

for tc in range(int(input())):
    N, W, H = map(int, input().split())
    brd = [list(map(int, input().split())) for _ in range(H)]
    answer = 0x9999999
    count = 0
    for i in range(H):
        for j in range(W):
            if brd[i][j]:
                count += 1
    tops = find_top(brd)
    for top in tops:
        solve(1, top, deepcopy(brd), count)
    print('#{} {}'.format(tc+1, answer))
