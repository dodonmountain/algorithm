import sys; sys.stdin = open('princess.txt')
from collections import deque
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))


def bfs():
    q = deque()
    q.append((0,0))
    visit = [[0] * M for _ in range(N)]
    gramend = 20000
    gramd = 20000
    grams = []
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1: continue
            if not visit[nx][ny]:
                if board[nx][ny] != 1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny))
                    if board[nx][ny] == 2:
                        gramd = visit[x][y] + ((N-1) - nx) + ((M-1) - ny) + 1
                        grams.append(gramd)
    if grams:
        gramend = min(grams)
    if gramend < visit[N-1][M-1]:
        return gramend
    return visit[N-1][M-1]


def solve(distance):
    if distance > T or distance == 0 or distance == 20000:
        print('Fail')
    else:
        print(distance)


N, M, T = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
solve(bfs())

