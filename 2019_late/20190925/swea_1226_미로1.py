import sys; sys.stdin = open('1226.txt')

def sfind(n):
    for i in range(16):
        for j in range(16):
            if maze[i][j] == n:
                return (i, j)

dx, dy = [1,0,-1,0], [0,1,0,-1]
def dfs(x, y):
    global flag
    visit[x][y] = 1
    for i in range(4):
        nx, ny = x, y
        if 0<= x + dx[i] < 16:
            nx = x + dx[i]
        if 0<= y + dy[i] < 16:
            ny = y + dy[i]
        if not visit[nx][ny]:
            if maze[nx][ny] == 3:
                flag = True
                return
            if maze[nx][ny] == 0:
                dfs(nx, ny)

for _ in range(10):
    t_case = int(input())
    maze = [list(map(int, list(input()))) for kk in range(16)]
    start = sfind(2)
    flag = False
    visit = [[0]*16 for _ in range(16)]
    dfs(start[0], start[1])
    print('#{} {}'.format(t_case, int(flag)))