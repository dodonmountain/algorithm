import sys
sys.stdin = open('2805.txt')

T = int(input())

for t_case in range(T):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, list(input()))))

    mid = (N-1)//2
    res = 0
    for i in range(N):
        for j in range(N):
            if i <= mid:
                if abs(mid-j) <= i:
                    res += board[i][j]
            else:
                if abs(mid-j) <= N-1-i:
                    res += board[i][j]
    print('#{} {}'.format(t_case+1, res))
