import sys
sys.stdin = open('5188.txt')



dx, dy = (1,0), (0,1)

def dfs(h,c):
    global tmp
    if h == (N-1,N-1):
        if c < tmp:
            tmp = c
        return
    for i in range(2):
        nx, ny = h[0], h[1]
        if 0 <= h[0] + dx[i] < N:
            nx = h[0] + dx[i]
        if 0 <= h[1] + dy[i] < N:
            ny = h[1] + dy[i]
        if not visit[nx][ny]:
            if c+board[nx][ny] <= tmp:
                visit[nx][ny] = 1
                dfs((nx,ny),c+board[nx][ny])
                visit[nx][ny] = 0

for t_case in range(int(input())):
    N = int(input())
    board,pp,ll = [],0,0
    for _ in range(N):
        board.append(list(map(int, input().split())))
    for i in range(1, N):
        pp += board[i][N-1];ll += board[i][0]
    if sum(board[0])+ pp > sum(board[N-1]) + ll:
        tmp = sum(board[N-1]) + ll
    tmp = sum(board[0]) + pp
    visit = [[0] * N for _ in range(N)]
    dfs((0,0),board[0][0])
    print('#{} {}'.format(t_case+1, tmp))