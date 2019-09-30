import sys; sys.stdin = open('1211.txt')
from pprint import pprint

def solve(x, y,init_y):
    global tmp, answer
    flag = 'down'
    dt = 0
    while True:
        if x == 99:
            if dt < tmp:
                tmp = dt
                answer = init_y
            return
        else:
            if flag == 'right':
                if board[x+1][y] == 1:
                    flag = 'down'
            elif flag == 'left':
                if board[x+1][y] == 1:
                    flag = 'down'
            else:
                if y + 1 < 100 and board[x][y+1] == 1:
                    flag = 'right'
                elif 0 <= y-1 and board[x][y-1] == 1:
                    flag = 'left'
                else:
                    flag = 'down'
        if flag == 'down':
            x += 1
            dt += 1
        elif flag == 'left':
            y -= 1
            dt += 1
        else:
            y += 1
            dt += 1


for __ in range(10):
    t_case = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    tmp = 987654321; answer = 0
    for i in range(100):
        if board[0][i] == 1:
            solve(0, i, i)
    print('#{} {}'.format(t_case, answer))

