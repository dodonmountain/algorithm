import sys;sys.stdin = open('2206.txt')

from collections import deque
delta = ((1,0), (0,1),(-1,0),(0,-1))
def bfs(s):
    global tmp, flag
    q=  deque();q.append(s)
    visit = [[[0]]*(M) for _ in range(N)]
    while q:
        x, y, is_break = q.popleft()
        for dx, dy in delta:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= N or ny < 0 or ny >= M:continue
            if not visit[nx][ny][0]:
                if (nx,ny) == (N-1, M-1):
                    tmp = D[x][y] + 1
                    flag = True
                    return
                if board[nx][ny] == 0:
                    visit[nx][ny][0] = visit[x][y][0] + 1
                    q.append((nx,ny,0))
N, M = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(N)]
cand = set()
res = 0x999999
flag = False
flag2 = False
bfs((0,0))
for x, y in list(cand):
    tmp = 0x9999999
    board[x][y] = 0
    bfs((0,0))
    board[x][y] = 1
    if flag:
        if tmp < res:
            flag2 = True
            res = tmp
if flag2:
    print(res+1)
else:
    print(-1)