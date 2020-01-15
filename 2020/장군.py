from pprint import pprint
import sys
sys.stdin = open('장군.txt')

sx, sy = map(int, input().split())
kx, ky = map(int, input().split())
delta = (
    ((-1, 0), (-2, -1), (-3, -2)),
    ((-1, 0), (-2, 1), (-3, 2)),
    ((0, -1), (-1, -2), (-2, -3)), 
    ((0, 1), (-1, 2), (-2, 3)), 
    ((0, -1), (1, -2), (2, -3)), 
    ((0, 1), (1, 2), (2, 3)), 
    ((1, 0), (2, -1), (3, -2)), 
    ((1, 0), (2, 1), (3, 2))
)
def bfs():
    from collections import deque
    q = deque()
    q.append((sx, sy))
    visit = [[-1] * 9 for _ in range(10)]
    visit[sx][sy] = 0
    while q:
        x, y = q.popleft()
        if (x, y) == (kx, ky):
            print(visit[kx][ky])
            return
        for path in delta:
            for i in range(3):
                dx, dy = path[i]
                nx, ny = x + dx, y + dy
                flag = True
                if nx < 0 or ny < 0 or nx > 9 or ny > 8:
                    flag = False
                    break
                if (nx, ny) == (kx, ky) and i < 2:
                    flag = False
                    break
            if flag and visit[nx][ny] == -1:
                visit[nx][ny] = visit[x][y] + 1
                q.append((nx, ny))
    print(-1)
bfs()
