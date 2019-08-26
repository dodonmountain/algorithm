import sys
sys.stdin = open("input.txt")
from pprint import pprint
T = int(input())

for t_case in range(T):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, list(input()))))
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                start = [i, j]
            elif maze[i][j] == 3:
                goal = (i, j)
                maze[i][j] = 0
    stack = [start]
    i, j = start[0], start[1]
    visited = [[0] * N for _ in range(N)]
    res = 0
    while stack:
        i,j = stack.pop()
        if i == goal[0] and j == goal[1]:
            res = 1
            visited[i][j] = 9
            break
        visited[i][j] = 1
        if i > 0:
            if maze[i - 1][j] == 0 and visited[i-1][j] ==0: # up
                stack.append((i - 1, j))
        if i < N - 1:
            if maze[i + 1][j] == 0 and visited[i+1][j] ==0: # down 
                stack.append((i + 1, j))
        if j < N - 1:
            if maze[i][j + 1] == 0 and visited[i][j+1] ==0: # right
                stack.append((i, j + 1))
        if j > 0:
            if maze[i][j - 1] == 0 and visited[i][j-1] ==0: # left
                stack.append((i, j - 1))
    print("#{} {}".format(t_case+1, res))