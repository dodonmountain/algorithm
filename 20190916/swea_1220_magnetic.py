import sys
sys.stdin = open('1220.txt')

for t_case in range(10):
    n = int(input())
    board = [list(input().split()) for _ in range(100)]
    board2 = []
    for i in range(100):
        tmp = ''
        for j in range(100):
            if board[j][i] != '0':
                tmp += board[j][i]
        board2.append(tmp)
    res = 0
    for i in board2:
        res += i.count('12')
    print('#{} {}'.format(t_case+1, res))