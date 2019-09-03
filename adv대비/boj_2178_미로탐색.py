import sys
sys.stdin = open('2178.txt')
from pprint import pprint
from collections import deque
N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, list(input()))))
pprint(maze,width=40)
def bfs(n,m):
    q = deque()
    visit = [[-1]*M for _ in range(N)]
    dx, dy = [1, 0, -1, 0],[0, 1, 0, -1]
    q.append((n,m))
    visit[n][m] = 99
    while q:
        here = q.popleft()
        for i in range(4):
            nx, ny = here[0] + dx[i], here[1] + dy[i]
            
        if visit[here[0]][here[1]] == -1 and board[here[0]][here[1]] == 1:

