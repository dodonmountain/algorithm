import sys
sys.stdin = open('tinput.txt')
from pprint import pprint
T = int(input())

for t_case in range(T):
    lines = []
    M, N, K = map(int, input().split())
    for _ in range(K):
        lines.append(list(map(int, input().split())))
    # lines = sorted(lines,key=lambda x:x[4])
    board = [[0] * (N+1) for _ in range(M+1)]
    for i in range(len(lines)):
        flag = 0
        height = lines[i][2] - lines[i][0] + 1
        width = lines[i][3] - lines[i][1] + 1
        for h in range(height):
            for w in range(width):
                if board[lines[i][0]+h][lines[i][1]+w] > lines[i][4]:
                    flag = 1
        for h in range(height):
            for w in range(width):
                if flag == 0:
                    board[lines[i][0]+h][lines[i][1]+w] = lines[i][4]
    checker = {
        0:0,
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
        6:0,
        7:0,
        8:0,
        9:0,
        10:0,
    }
    for i in range(M):
        for j in range(N):
            checker[board[i][j]] += 1
    print('#{} {}'.format(t_case+1, max(checker.values())))


