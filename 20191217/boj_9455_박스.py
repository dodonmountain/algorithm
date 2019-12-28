import sys
sys.stdin = open('9455.txt')

T = int(input())

for tc in range(T):
    m, n = map(int, input().split())
    answer = 0
    board = [list(map(int, input().split())) for _ in range(m)]
    starter = []
    for i in range(m-1):
        for j in range(n):
            if board[i][j] == 1:
                starter.append((i,j))
    for x, y in starter:
        cnt = 0
        for i in range(x, m):
            if board[i][y] == 0:
                cnt += 1
        answer += cnt
    print(answer)