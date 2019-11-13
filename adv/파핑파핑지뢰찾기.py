from collections import deque
from pprint import pprint
import sys
sys.stdin = open('minesweeper.txt')


delta = ((1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1))

def search(x, y):
    mine = 0

    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
            continue
        if board[nx][ny] == '*':
            mine += 1
    return mine

def bfs(s):
    q = deque()
    q.append(s)
    visit = [[0] * N for _ in range(N)]
    visit[s[0]][s[1]] = 1
    while q:
        x, y = q.popleft()
        mine = search(x, y)
        board[x][y] = mine
        if not mine:
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                    continue
                if not visit[nx][ny] and board[nx][ny] =='.':
                    visit[nx][ny] = 1
                    board[nx][ny] = 0
                    q.append((nx, ny))


T = int(input())

for tc in range(T):
    N = int(input())
    cnt = 0
    board = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                if not search(i,j):
                    bfs((i, j))
                    cnt += 1
    for i in range(N):
        for j in range(N):
            if board[i][j] == '.':
                cnt += 1
    print('#{} {}'.format(tc+1, cnt))