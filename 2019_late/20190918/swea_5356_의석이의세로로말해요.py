import sys
sys.stdin = open('5356.txt')

T = int(input())

for t_case in range(T):
    board = [list(input()) for _ in range(5)]
    mx = max(map(len, board))
    for i in board:
        if len(i) < mx:
            i.extend([-1]*(mx-len(i)))
    res = ''
    for i in range(mx):
        for j in range(5):
            if board[j][i] != -1:
                res += board[j][i]
    print('#{} {}'.format(t_case+1, res))