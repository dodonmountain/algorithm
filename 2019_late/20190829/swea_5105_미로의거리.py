import sys
sys.stdin = open('5105.txt')
from pprint import pprint
from collections import deque


from collections import deque


def bfs(x, y):
    global shortest
    Q = deque()
    visit[x][y] == True
    Q.append((x, y))
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    D = [[0] * N for _ in range(N)] # 최단 거리를 저장
    while Q:
        xx, yy = Q.popleft()
        for step in range(4):
            nx = xx + dx[step]
            ny = yy + dy[step]

            if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:
                continue
            if maze[nx][ny] == 3:
                shortest = D[xx][yy]
                return
            if maze[nx][ny] == 0 and visit[nx][ny] == False:
                visit[nx][ny] = 1  # 방문표시
                D[nx][ny] = D[xx][yy] + 1
                Q.append((nx, ny))


T = int(input())

for t_case in range(T):
    shortest = 0
    N = int(input())
    visit = [[0] * N for _ in range(N)]
    maze = []
    for _ in range(N):
        maze.append(list(map(int,input())))
    # pprint(maze, width=30)
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
            elif maze[i][j] == 3:
                goal = [i, j]
    bfs(start[0], start[1])
    pprint(visit,width=40)
    print('#{} {}'.format(t_case + 1, shortest))



