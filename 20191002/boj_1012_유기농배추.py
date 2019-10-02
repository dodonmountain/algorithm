import sys;sys.stdin = open('1012.txt')
from pprint import pprint

from collections import deque

dx, dy = [1, 0 ,-1, 0], [0, 1, 0, -1]
def bfs(s):
    q = deque()
    q.append(s)
    visit[s[0]][s[1]] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x, y
            if 0 <= x + dx[i] < N:nx = x + dx[i]
            if 0 <= y + dy[i] < M:ny = y + dy[i]
            if not visit[nx][ny] and board[nx][ny] == 1:
                visit[nx][ny] = 1
                q.append((nx, ny))
    
for t_case in range(int(input())):
    M, N, K = map(int, input().split())
    board = [[0] * M for _ in range(N)]
    for i in range(K):
        a, b = map(int, input().split())
        board[b][a] = 1
    cnt = 0
    visit = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visit[i][j] != 1:
                start = (i, j)
                bfs(start)
                cnt += 1
    print(cnt)
    
    
