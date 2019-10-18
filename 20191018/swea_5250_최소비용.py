import sys;sys.stdin=open('5250.txt')



delta = ((0,1), (1,0), (-1,0), (0,-1))

def dfs(s,d):
    global mn
    x, y = s
    if (x, y) == (N-1, N-1):
        if d < mn:
            mn = d 
        return
    save_d = d
    for dx, dy in delta:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1:continue
        if board[nx][ny] > board[x][y]:
            d += board[nx][ny] - board[x][y]
        d += 1
        if d < mn:
            dfs((nx,ny),d)
        d = save_d

T = int(input())

for t_case in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    mn = 0
    for i in range(1, N):
        prev =  board[0][i-1]
        if board[0][i] > prev:
            mn += (board[0][i] - prev) + 1
        else:
            mn += 1
    for i in range(1, N):
        prev = board[i-1][N-1]
        if board[i][N-1] > prev:
            mn += (board[i][N-1] - prev) + 1
        else:
            mn += 1
    dfs((0,0),0)
    print('#{} {}'.format(t_case+1, mn))
