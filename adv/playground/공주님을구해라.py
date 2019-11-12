import sys; sys.stdin = open('princess.txt')
from collections import deque
delta = ((1, 0), (0, 1), (-1, 0), (0, -1))


def bfs():
    q = deque()
    q.append((0,0))
    visit = [[-1] * M for _ in range(N)]
    visit[0][0] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > N-1 or ny > M-1: continue
            if visit[nx][ny] == -1:
                if board[nx][ny] != 1:
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx,ny))
    if visit[N-1][M-1] != -1:
        distance1 = visit[N-1][M-1]
    else:
        distance1 = 20000000
    gram = []
    for i in range(N):
        for j in range(M):
            if board[i][j] == 2 and visit[i][j] != -1:
                gram.append([i, j, visit[i][j]])
    if gram:
        gram.sort(key=lambda x:x[2])
        shortest_gram = gram[0]
        q.append((shortest_gram[0],shortest_gram[1]))
        g_visit = [[-1] * M for _ in range(N)]
        g_visit[shortest_gram[0]][shortest_gram[1]] = shortest_gram[2]
        while q:
            x, y = q.popleft()
            for dx, dy in delta:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx > N-1 or ny > M-1: continue
                if g_visit[nx][ny] == -1:
                    g_visit[nx][ny] = g_visit[x][y] + 1
                    q.append((nx,ny))
        distance2 = g_visit[N-1][M-1]
        if distance1 < distance2:
            distance = distance1
        else:
            distance = distance2
    else:
        distance = distance1
    if distance > T or distance == -1:
        print('Fail')
    else:
        print(distance)


N, M, T = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
bfs()

