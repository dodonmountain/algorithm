from pprint import pprint
import sys
sys.stdin = open('오셀로.txt')

T = int(input())
delta = ((0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))
for t_case in range(T):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    mid = n >> 1
    board[mid][mid] = 2
    board[mid-1][mid-1] = 2
    board[mid-1][mid] = 1
    board[mid][mid-1] = 1
    for i in range(m):
        x, y, c = map(int, input().split())
        y, x = y-1, x-1
        # 8방향 탐색
        reverse = []
        for i in range(8):
            dx, dy = delta[i]
            nx, ny = x + dx, y + dy
            while True:
                if nx < 0 or ny < 0 or nx > n-1 or ny > n-1:
                    reverse = []
                    break
                if board[nx][ny] == 0:
                    reverse = [] 
                    break
                if board[nx][ny]==c:
                    break
                else:
                    reverse.append((nx,ny))
                nx, ny = nx + dx, ny + dy
            for rx, ry in reverse:
                if c == 1:
                    board[rx][ry] = 1
                else:
                    board[rx][ry] = 2
        board[x][y] = c
    w, b = 0, 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                w += 1
            elif board[i][j] == 2:
                b += 1
    print('#{} {} {}'.format(t_case+1 ,w ,b))

