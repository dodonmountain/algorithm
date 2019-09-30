import sys;sys.stdin = open('2819.txt')
dx, dy = [1,0,-1,0], [0,1,0,-1]

def dfs(x, y, arr, d):
    if d == 7:
        tmp = ''.join(list(map(str, arr)))
        s_arr.add(tmp)
        return
    else:
        for i in range(4):
            nx, ny = x, y
            if 0 <= x + dx[i] < 4:nx = x + dx[i]
            if 0 <= y + dy[i] < 4:ny = y + dy[i]
            if (x,y) != (nx,ny):
                dfs(nx, ny, arr + [board[nx][ny]], d + 1)
for t_case in range(int(input())):
    s_arr = set()
    board = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            dfs(i, j, [], 0)
    print('#{} {}'.format(t_case+1, len(s_arr)))