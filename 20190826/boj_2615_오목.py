import sys
sys.stdin = open('inputb.txt')
from pprint import pprint

board = []
flag=0
for lines in range(19):
    board.append(list(map(int,input().split())))
# pprint(board,width=190)
for garo in board:
    for i in range(14):
        if garo[i] != 0:
            if garo[i] == garo[i+1] == garo[i+2] == garo[i+3] == garo[i+4] != garo[i+5]:
                print(garo[i])
                flag = 1
for sero in range(19):
    for i in range(15):
        if board[i][sero] != 0:
            if board[i][sero] == board[i+1][sero] ==board[i+2][sero] == board[i+3][sero] == board[i+4][sero] != board[i+5][sero]:
                print(board[i][sero])
                flag = 1
for i in range(14):
    for j in range(14):
        if board[i][j] != 0:
            if board[i][j] == board[i+1][j+1] == board[i+2][j+2] == board[i + 3][j+3] == board[i + 4][j+4] != board[i +5][j+5]:
                print(board[i][j])
                print(i+1,j+1)
                flag = 1
for i in range(18,5,-1):
    for j in range(18,5,-1):
        if board[i][j] != 0:
            if board[i][j] == board[i-1][j-1] == board[i-2][j-2] == board[i - 3][j-3] == board[i - 4][j-4] != board[i -5][j-5]:
                print(board[i][j])
                print(i-1,j-1)
                flag = 1
if flag == 0:
    print(0)