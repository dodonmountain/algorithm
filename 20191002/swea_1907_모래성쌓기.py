import sys;sys.stdin = open('1907.txt')
from pprint import pprint

delta = ((1,0),(1,1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1),(1,-1))



        
for t_case in range(int(input())):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    wave = 0
    starter = set()
    for i in range(H-1):
        for j in range(W-1):
            if board[i][j] == '.':
                starter.add((i,j))
    tmp = set()
    while True:
        for i in starter:
            x, y = i
            flag =False
            for dx, dy in delta:
                nx, ny = x, y
                if 0 <= x + dx < H: nx = x + dx
                if 0 <= y + dy < W: ny = y + dy
                if board[nx][ny] != '.':
                    board[nx][ny] = int(board[nx][ny]) - 1
            for dx, dy in delta:
                nx, ny = x, y
                if 0 <= x + dx < H: nx = x + dx
                if 0 <= y + dy < W: ny = y + dy
                if board[nx][ny] != '.':
                    if board[nx][ny] == 0:
                        board[nx][ny] = '.'
                        tmp.add((nx,ny))
                    else:
                        board[nx][ny] = int(board[nx][ny]) + 1
        if not tmp:
            break
        else:
            starter = tmp
            tmp = set()
    print(wave)
    
