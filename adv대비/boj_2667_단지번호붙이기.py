import sys
sys.stdin = open('2667.txt')
from pprint import pprint
N = int(input())
board = []

for _ in range(N):
    board.append(list(map(int, list(input()))))
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
number = 0
visit = [[-1] * N for _ in range(N)]
def dfs(sx,sy):
    stack, res = [], 0
    global visit
    stack.append((sx,sy))
    while stack:
        here = stack.pop()
        if board[here[0]][here[1]] == 1:
            for i in range(4):
                if N-1 < here[0]+dx[i] or 0 > here[0]+dx[i]:
                    continue
                else:
                    nx = here[0]+dx[i]
                if N-1 < here[1] + dy[i] or 0 > here[1] + dy[i]:
                    continue
                else:
                    ny = here[1] + dy[i]
                if visit[nx][ny] == -1 and board[nx][ny] == 1:
                    visit[nx][ny] = 99
                    stack.append((nx,ny))
                    res += 1
    return res
a = []
for j in range(N):
    for i in range(N):
        if visit[i][j] != 99 and board[i][j] == 1:
            a.append(dfs(i,j))
print(len(a))
for i in sorted(a):
    if i == 0:
        print(1)
    else:
        print(i)

