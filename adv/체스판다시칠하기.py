import sys;sys.stdin=open('chess.txt')

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def solve(s):
    x, y = s
    cnt = 0
    for i in range(8):
        for j in range(7):
            if board[i][j] == board[i][j+1]:
                cnt += 1
    print(cnt)


for i in range(N):
    for j in range(M):
        if i + 7 < N and j + 7 < M:
            solve(((i, j)))
