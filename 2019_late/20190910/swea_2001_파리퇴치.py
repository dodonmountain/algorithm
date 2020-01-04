import sys
sys.stdin = open("2001.txt")

T = int(input())

for t_case in range(T):
    N, M = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    tmp = -1
    res = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            if tmp < res:
                tmp = res
            res = 0
            for w in range(M):
                for h in range(M):
                    res += board[i+h][j+w]
    print('#{} {}'.format(t_case+1, tmp))
