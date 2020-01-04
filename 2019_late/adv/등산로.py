import sys;sys.stdin = open('등산로.txt')
from pprint import pprint



delta = ((1,0),(0,1),(-1,0),(0,-1))

def dfs(s, path, v):
    global longest
    if path > longest:
        longest = path
    x, y = s
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:continue
        if v[nx][ny] == -1:
            if board[nx][ny] < board[x][y]:
                v[nx][ny] = 1
                dfs((nx,ny), path+1, v)
                v[nx][ny] = -1


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    high = max(list(map(max, board)))
    longest = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == high:
                for cx in range(N):
                    for cy in range(N):
                        for depth in range(0, K + 1):
                                visit = [[-1] * N for _ in range(N)]
                                visit[i][j] = 1
                                board[cx][cy] -= depth
                                dfs((i, j),1, visit)
                                board[cx][cy] += depth
    print('#{} {}'.format(tc, longest))
