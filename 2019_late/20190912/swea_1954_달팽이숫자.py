import sys
sys.stdin = open('1954.txt')
from pprint import pprint

T = int(input())

for t_case in range(T):
    N = int(input())
    if N == 1:
        print('#{}'.format(t_case+1))
        print(1)
        continue
    board = [[0]*N for _ in range(N)]
    flag = True
    move = {'right': 1, 'down': 0, 'left':0, 'up': 0}
    k,i,j = 2,0,0
    board[0][0] = 1
    while flag:
        if move['right']:
            if j < N - 1 and board[i][j+1] == 0:
                board[i][j+1] = k
                j += 1
                k += 1
            else:
                if board[i+1][j]:
                    flag = False
                move['right'] = 0
                move['down'] = 1

        elif move['down']:
            if i  < N - 1 and board[i+1][j] == 0:
                board[i+1][j] = k
                i += 1
                k += 1
            else:
                if board[i][j-1]:
                    flag = False
                move['down'] = 0
                move['left'] = 1

        elif move['left']:
            if 0 <= j - 1 and board[i][j-1] == 0:
                board[i][j-1] = k
                j -= 1
                k += 1
            else:
                if board[i-1][j]:
                    flag = False
                move['left'] = 0
                move['up'] = 1

        elif move['up']:
            if 0 <= i - 1 and board[i-1][j] == 0:
                board[i-1][j] = k
                i -= 1
                k += 1
            else:
                if board[i][j+1]:
                    flag = False
                move['up'] = 0
                move['right'] = 1

    print('#{}'.format(t_case+1))
    for i in board:
        print(*i)
