import sys
sys.stdin = open('1209.txt')

T = 10

for t_case in range(10):
    trash = input()
    board = [list(map(int, input().split())) for _ in range(100)]
    comp, board2 = [], []
    for i in range(100):
        tmp = []
        for j in range(100):
            tmp.append(board[j][i])
        board2.append(tmp)
    tmp1,tmp2 = 0,0
    for i in range(100):
        tmp1 += board[i][i]
        tmp2 += board2[i][i]
    comp.extend(list(map(sum, board)))
    comp.extend(list(map(sum, board2)))
    comp.append(tmp1);comp.append(tmp2)
    print('#{} {}'.format(t_case+1, max(comp)))