import sys;sys.stdin = open('1907.txt')
from pprint import pprint

from collections import deque

def check(x, y):
    cnt = 0
    for dx, dy in ((1,0),(1,1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1),(1,-1)):
        nx, ny = x, y
        if 0 <= x + dx < H: nx = x + dx
        if 0 <= y + dy < W: ny = y + dy
        if board[nx][ny] == -1:
            cnt += 1
    if cnt >= board[x][y]:
        return True
    return False

def wave():
    cnt = 0
    tmp = []
    while q:
        x, y= q.popleft()
        board[x][y] = -1
        for dx, dy in ((1,0),(1,1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1),(1,-1)):
            if 0 <= x + dx < H: nx = x + dx
            if 0 <= y + dy < W: ny = y + dy
            if board[nx][ny] != -1:
                if board[nx][ny] != 9:
                    if check(nx,ny):
                        if not visit[nx][ny]:
                            tmp.append((nx, ny))
        if not q:
            if tmp:
                q.extend(tmp)
                cnt += 1
                tmp = []
    return cnt + 1


H, W = map(int, input().split())
board = [list(input()) for _ in range(H)]
q = deque()
visit = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if board[i][j] == '.':
            board[i][j] = -1
        else:
            board[i][j] = int(board[i][j])
for i in range(H):
    for j in range(W):
        if board[i][j] != -1:
            if check(i, j):
                q.append((i,j))
                visit[i][j] = 1
print(wave)
