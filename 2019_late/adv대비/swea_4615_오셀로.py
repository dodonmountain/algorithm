import sys
sys.stdin = open('4615.txt')
from pprint import pprint

# T = int(input())
T = 1

for t_case in range(T):
    # N, M = map(int, input().split())
    N = 6
    M = int(input())
    act = []
    for _ in range(M):
        act.append(list(map(int, input().split())))
    board = [[0] * N for x in range(N)]
    board[N//2][N//2],board[N // 2 - 1][N // 2 - 1],board[N // 2 - 1][N // 2],board[N // 2][N // 2 - 1] = 2,2,1,1
    pprint(board)
    color = 2
    for acts in act:
        if color == 2:
            color = 1
        else:
            color = 2
        # print(acts)
        y = acts[0] - 1
        x = acts[1] - 1
        # color = acts[2]
        board[y][x] = color
        stack = []
        if x >= y:
            upleft = y
        else:
            upleft = x
        if (N - 1 - x) <= (N -1 - y):
            upright = (N -1 - y)
        else:
            upright = (N -1 - x)
        downleft = N- y - 1
        if (N - 1 - y) <= (N - 1 - x):
            downright = N - 1 - y
        else:
            downright = N - 1 - x
        #check down
        if y < N - 1:
            # print('cdown')
            for i in range(1, N-y):
                if board[y+i][x] != color and board[y+i][x] !=0:
                    stack.append(i)
                elif board[y + i][x] == color:
                    break
                else:
                    stack.clear()
                    break
                if (y+i) == N-1 or board[y+1][x] == 0:
                    stack.clear()
                    break
            if stack:
                for reverse in stack:
                    board[y+reverse][x] = color
                stack.clear()

        #check up
        if y > 0:
            # print('cup')
            for i in range(1, y + 1):
                if board[y-i][x] != color and board[y-i][x] != 0:
                    stack.append(i)
                elif board[y-i][x] == color:
                    break
                else:
                    stack.clear()
                    break
                if (y-i) == 0 or board[y-1][x] == 0:
                    stack.clear()
                    break
            if stack:
                for reverse in stack:
                    board[y-reverse][x] = color
                stack.clear()
        #check left
        if x > 0:
            # print('cleft')
            for i in range(1, x+1):
                if board[y][x-i] != color and board[y][x-i] != 0:
                    stack.append(i)
                elif board[y][x - i] == color:
                    break
                else:
                    stack.clear()
                    break
                if (x-1) == 0 or board[y][x-1] == 0:
                    stack.clear()
            if stack:
                for reverse in stack:
                    board[y][x-reverse] = color
                stack.clear()
        # check right
        if x < N - 1:
            # print('cright')
            for i in range(1, N-x):
                if stack:
                    if board[y][x+i] != color:
                        stack.clear()
                        break
                if board[y][x+i] != color and board[y][x+i] !=0 :
                    stack.append(i)
                elif board[y][x+i] == color:
                    break
                else:
                    stack.clear()
                if (x+1) == N-1 or board[y][x+1] == 0:
                    stack.clear()
            if stack:
                for reverse in stack:
                    board[y][x+reverse] = color
                    stack.clear()
        # check upright
        if x < N - 1 and y > 0:
            # print('cupright')
            for i in range(1, upright):
                if board[y-i][x+i] != color and board[y-i][x+i] != 0:
                    stack.append(i)
                elif board[y-i][x + i] == color:
                    break
                else:
                    stack.clear()
                    break
                if (x+1) == N or y-1 ==0  or board[y-i][x+i] == 0:
                    stack.clear()
            if stack:
                for reverse in stack:
                    board[y-reverse][x+reverse] = color
                stack.clear()
        # check upleft
        if x > 0 and y > 0:
            # print('cupleft')
            for i in range(1, upleft+1):
                if board[y-i][x-i] != color and board[y-i][x-i] != 0:
                    stack.append(i)
                elif board[y-i][x - i] == color:
                    break
                else:
                    stack.clear()
                    break
                if (x-1) == 0 or y-1 ==0  or board[y-i][x-i] == 0:
                    stack.clear()
            if stack:
                for reverse in stack:
                    board[y-reverse][x-reverse] = color
                stack.clear()
        # check downright:
        if y < N - 1 and x < N - 1:
            # print('cdownright')
            for i in range(1, downright+1):
                if board[y+i][x+i] != color and board[y+i][x+i] != 0:
                    stack.append(i)
                elif board[y+i][x + i] == color:
                    break
                if board[y+i][x+i] == 0 or y+i == N - 1:
                    stack.clear()
            if stack:
                for reverse in stack:
                    board[y+reverse][x+reverse] = color
                stack.clear()
        # check downleft
        if y < N - 1 and x > 0:
            # print('cdownleft')
            for i in range(1, downleft+1):
                if board[y+i][x-i] != color and board[y+i][x-i] != 0:
                    stack.append(i)
                elif board[y + i][x - i] == color:
                    break
                if board[y + i][x - i] == 0 or y + i == N-1:
                    stack.clear()
                    break
                if (x-1) == 0 or y+1 == N-1  or board[y+i][x-i] == 0:
                    stack.clear()
            if stack:
                for reverse in stack:
                    board[y+reverse][x-reverse] = color
                stack.clear()
        # pprint(board,width=60)
    black, white = 0, 0
    for i in board:
        black += i.count(1)
        white += i.count(2)
    for i in range(6):
        for j in range(6):
            if board[i][j] == 0:
                board[i][j] = '.'
            elif board[i][j] == 1:
                board[i][j] = 'B'
            else:
                board[i][j] = 'W'
    for i in range(6):
        print(*board[i])
    if black > white:
        print("Black")
    else:
        print("White")
    # print("#{} {} {}".format(t_case+1, black,white))