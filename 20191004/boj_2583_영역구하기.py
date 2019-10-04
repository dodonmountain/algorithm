import sys;sys.stdin = open('2583.txt')
from pprint import pprint

from collections import deque
delta = ((1,0), (0,1),(-1,0),(0,-1))
def bfs(s):
    area = 0
    q=  deque();q.append(s)
    visit[s[0]][s[1]] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N:continue
            if not visit[nx][ny]:
                if board[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                    area += 1
    return area + 1
M, N, K = map(int, input().split())
board = [[0] * (N) for _ in range(M)]
for i in range(K):
    rect = list(map(int, input().split()))
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    for i in range(height):
        for j in range(width):
            board[M - rect[3] + i][rect[0] + j] = 1
visit = [[0] * (N) for _ in range(M)]
result = [];cnt = 0
for i in range(M):
    for j in range(N):
        if board[i][j] == 0 and not visit[i][j]:
            result.append(bfs((i,j)))
            cnt += 1
result.sort()
print(cnt)
print(*result)
