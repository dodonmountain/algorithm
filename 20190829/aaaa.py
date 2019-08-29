import sys
sys.stdin = open('5105.txt', 'r')

import collections
Q = collections.deque()

def entrance():
    global goal
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j
            elif maze[i][j] == 3:
                goal = 2
                return i, j

dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]

for t in range(1, int(input()) + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    distances = [[0] * N for _ in range(N)]
    success = False
    goal = 3

    y_i, x_i = entrance()
    Q.append((y_i, x_i))
    visited[y_i][x_i] = 1
    while Q:
        y, x = Q.popleft()
        if maze[y][x] == goal:
            success = True
            break
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx] and maze[ny][nx] != 1:
                visited[ny][nx] = 1
                distances[ny][nx] = distances[y][x] + 1
                Q.append((ny, nx))
        print(Q)
        for i in range(N):
            print(i,':',visited[i])
        print()

    if success:
        print('#{} {}'.format(t, distances[y][x] - 1))
    else:
        print('#{} 0'.format(t))