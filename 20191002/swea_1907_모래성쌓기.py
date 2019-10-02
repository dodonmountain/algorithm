import sys;sys.stdin = open('1907.txt')
from pprint import pprint
from time import time
stime = time()

delta = ((1,0),(1,1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1),(1,-1))
        
from collections import deque
 
def check():
    for x in range(H-1):
        for y in range(W-1):
            if board[x][y] != 0:
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or ny <0 or nx >= H or ny >= W:continue
                    if not board[nx][ny]:
                        mirror_board[x][y] += 1
                if int(board[x][y]) <= mirror_board[x][y]:
                    q.append((x, y))
                    visit[x][y] = 1
def wave():
    global q
    answer = 0
    tmp = deque()
    while q:
        x, y = q.popleft()
        board[x][y] = '.'
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny <0 or nx >= H or ny >= W:continue
            if board[nx][ny] != 0 and not visit[nx][ny]:
                mirror_board[nx][ny] += 1
                if int(board[nx][ny]) <= mirror_board[nx][ny]:
                    tmp.append((nx, ny))
                    visit[nx][ny] = 1
        if not q:
            q, tmp = tmp, q
            answer += 1
    return answer

for t_case in range(int(input())):
    H, W = map(int, input().split())
    board = []
    for i in range(H):
        board.append(list(map(int, list(input().replace(".", "0")))))
    mirror_board = [[0] * W for _ in range(H)]
    visit = [[0] * W for _ in range(H)]   
    answer = 0
    q = deque()
    for i in range(H-1):
        for j in range(W-1):
            if board[i][j] == 0:
                visit[i][j] = 1
    check()
    print('#{} {}'.format(t_case+1, wave()))
print(time() - stime)