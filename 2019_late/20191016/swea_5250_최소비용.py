import sys;sys.stdin=open('5250.txt')


from collections import deque
delta = [(0,1), (1,0), (0,-1),(-1,0)]

def bfs():
    q= deque()
    q.append((0,0))
    D = [[0x9999999] * N for _ in range(N)]
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if 0 < nx or 0 < ny or nx > N-1 or ny > N-1:continue
            D[nx][ny] = D[x][y] + board[x][y] + 1
            q.append((nx,ny))
            if (nx, ny) == (N-1,N-1):
                print(D[N-1][N-1])
                return
for t_case in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    bfs()