import sys;sys.stdin=open('2178.txt')

from collections import deque

delta = ((0,1),(1,0),(0,-1),(-1,0))
def bfs():
    q = deque();q.append((0,0))
    visit = [[0] *(M+1) for _ in range(N+1)]
    visit[0][0] = 1
    D = [[0] *(M+1) for _ in range(N+1)]
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > N - 1 or ny < 0 or ny > M - 1: continue
            if not visit[nx][ny]:
                if board[nx][ny] == 1:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
                    D[nx][ny] = D[x][y] + 1
    print(D[N-1][M-1]+1)


N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
bfs()
