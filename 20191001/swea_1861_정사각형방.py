import sys; sys.stdin = open('1861.txt')
from pprint import pprint
from collections import deque

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
def bfs(s):
    global tmp
    q = deque()
    q.append(s)
    visit = [[0] * N for _ in range(N)]
    visit[s[0]][s[1]] = 1
    D = [[0] * N for _ in range(N)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x, y
            if 0 <= x + dx[i] < N:nx = x + dx[i]
            if 0 <= y + dy[i] < N:ny = y + dy[i]
            if not visit[nx][ny]:
                if board[nx][ny] - board[x][y] == 1:
                    visit[nx][ny] = 1
                    candidate[nx][ny] = 1
                    q.append((nx,ny))
                    D[nx][ny] = D[x][y] + 1
    tmp = max(map(max, D)) + 1

for t_case in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    start = 0x9999999
    candidate = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not candidate[i][j]:
                tmp = 0
                bfs((i,j))
                if tmp > answer:
                    answer = tmp
                    start = board[i][j]
                elif tmp == answer:
                    if start > board[i][j]:
                        start = board[i][j]
    print('#{} {} {}'.format(t_case+1, start, answer))