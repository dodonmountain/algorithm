import sys;sys.stdin = open('7576.txt')
from pprint import pprint


from collections import deque
delta = ((1,0), (0,1),(-1,0),(0,-1))
def bfs():
    global q, visit
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:continue
            if not visit[nx][ny] and board[nx][ny] == 0:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx,ny))


M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
visit  = [[0] * M for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if board[i][j] == -1:
            visit[i][j] = -1
        elif board[i][j] == 1:
            visit[i][j] = 1
            for dx, dy in delta:
                nx, ny = i + dx, j + dy
                if nx < 0 or nx >= N or ny < 0 or ny >= M:continue
                if board[nx][ny] == 0 and not visit[nx][ny]:
                    q.append((nx,ny))
                    visit[nx][ny] = 1

if not q:
    print(0)
else:
    bfs()
    flag = False
    if not flag:
        for i in range(N):
            for j in range(M):
                if visit[i][j] == 0:
                    flag = True
                    break
    if flag:
        print(-1)
    else:
        print(max(map(max, visit)))

    
                