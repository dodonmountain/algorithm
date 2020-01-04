import sys; sys.stdin = open('2210.txt')


board = [list(input().split()) for _ in range(5)]
dx, dy = [1,0,-1,0], [0,1,0,-1]
s_arr = set()
def dfs(x, y, arr, d):
    if d == 6:
        word = ''
        for i in arr:
            word += i
        if word not in s_arr:
            s_arr.add(word)
        return
    else:
        for i in range(4):
            nx, ny = x, y
            if 0 <= x + dx[i] < 5:nx = x + dx[i]
            if 0 <= y + dy[i] < 5:ny = y + dy[i]
            if (x,y) != (nx,ny):
                dfs(nx, ny, arr + [board[nx][ny]], d + 1)

for i in range(5):
    for j in range(5):
        dfs(i, j, [board[i][j]],1)
print(len(s_arr))

