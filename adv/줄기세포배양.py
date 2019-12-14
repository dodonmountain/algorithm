import sys;sys.stdin = open('stemcell.txt')
from pprint import pprint


T = int(input())

for tc in range(1, T):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            board[i][j] = (2, board[i][j])
    pprint(board, width=M*10)
    