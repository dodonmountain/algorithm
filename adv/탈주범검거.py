import sys;sys.stdin=open('talju.txt')
from pprint import pprint 

from collections import deque
def bfs(s):
    q = deque()
    q.append(s)
    visit = [[0] * M for _ in range(N)]
    visit[s[0]][s[1]] = 1
    while q:
        x, y = q.popleft()
        delta = tunnel[board[x][y]]
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1:continue
            if (-dx, -dy) not in tunnel[board[nx][ny]]:continue
            if not visit[nx][ny]:
                if board[nx][ny] != 0:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx,ny))
    cnt = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j] != 0 and visit[i][j] <= L:
                cnt += 1
    print('#{} {}'.format(tc+1, cnt))

tunnel ={
    0 : (),
    1 : ((1, 0),(0, 1),(-1, 0),(0, -1)),
    2 : ((1, 0), (-1, 0)),
    3 : ((0, 1), (0, -1)),
    4 : ((-1, 0), (0, 1)),
    5 : ((1, 0), (0, 1)),
    6 : ((1, 0), (0, -1)),
    7 : ((-1, 0), (0, -1))
}

T = int(input())

for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    manhole = (R, C)
    bfs(manhole)
