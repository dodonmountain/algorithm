import sys
sys.stdin = open('1974.txt')

T = int(input())

for t_case in range(T):
    board = []
    flag = True
    for _ in range(9):
        board.append(list(map(int, input().split())))
    for line in board:
        if len(set(line)) < 9:
            flag = False
    if flag:
        for i in range(9):
            tmp = []
            for j in range(9):
                tmp.append(board[j][i])
            if len(set(tmp)) < 9:
                flag = False
                break
    if flag:
        for k in range(0, 7 , 3):
            for l in range(0,7,3):
                tmp = []
                for i in range(3):
                    for j in range(3):
                        tmp.append(board[k+i][l+j])
                if len(set(tmp)) < 9:
                    flag = False
                    break
    print('#{} {}'.format(t_case+1, int(flag)))