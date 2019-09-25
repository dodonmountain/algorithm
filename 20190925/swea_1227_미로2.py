import sys; sys.stdin = open('1227.txt')
from collections import deque
def sfind(n):
    for i in range(100):
        for j in range(100):
            if maze[i][j] == n:
                return (i, j)

dx, dy = [1,0,-1,0], [0,1,0,-1]
def bfs(x, y):
    q = deque()
    visit[x][y] = 1
    q.append((x,y))
    while q:
        here = q.popleft()
        x, y = here[0], here[1]
        for i in range(4):
            nx, ny = x, y
            if 0 <= x + dx[i] < 100:
                nx = x + dx[i]
            if 0 <= y + dy[i] < 100:
                ny = y + dy[i]
            if not visit[nx][ny]:
                if maze[nx][ny] == 3:
                    return True
                if maze[nx][ny] == 0:
                    visit[nx][ny] = 1
                    q.append((nx,ny))
    return False
for t in range(10):
    t_case = int(input())
    maze = [list(map(int, list(input()))) for _ in range(100)]
    start = sfind(2)
    visit = [[0] * 100 for _ in range(100)]
    if bfs(start[0], start[1]):
        print('#{} {}'.format(t_case, 1))
    else:
        print('#{} {}'.format(t_case, 0))