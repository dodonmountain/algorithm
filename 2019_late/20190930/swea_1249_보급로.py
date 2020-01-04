import sys;sys.stdin = open('1249.txt')

from collections import deque
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
def bfs(s):
    q = deque()
    visit = [[0] * N for _ in range(N)]
    q.append(s)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x, y
            if 0 <= x + dx[i] < N:nx = x + dx[i]
            if 0 <= y + dy[i] < N:ny = y + dy[i]
            if not visit[nx][ny]:
                visit[nx][ny] = 1
                if (nx, ny) == (N-1, N-1):
                    print(visit)
                q.append((nx,ny))
        

for t_case in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    bfs((0,0))