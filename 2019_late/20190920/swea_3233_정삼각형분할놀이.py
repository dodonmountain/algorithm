import sys; sys.stdin = open('1227.txt')

def sfind(n):
    for i in range(100):
        for j in range(100):
            if maze[i][j] == n:
                return (i, j)

dx, dy = [1,0,-1,0], [0,1,0,-1]
def dfs(x, y):
    if maze[x][y] == 3:
        print('야호')
        return
    visit[x][y] = 1
    for i in range(4):
        nx, ny = x, y
        if 0 <= x + dx[i] < 100:
            nx = x + dx[i]
        if 0 <= y + dy[i] < 100:
            ny = y + dy[i]
        if maze[nx][ny] == 0 or maze[nx][ny] == 3:
            if not visit[nx][ny]:
                dfs(nx, ny)
for t in range(1):
    t_case = int(input())
    maze = [list(map(int, list(input()))) for _ in range(100)]
    start = sfind(2)
    visit = [[0] * 100 for _ in range(100)]
    dfs(start[0], start[1])