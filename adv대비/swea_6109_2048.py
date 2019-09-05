import sys
sys.stdin = open('6109.txt')
from pprint import pprint

T = int(input())
T = 1
def rotate(a):
    n = len(a)
    copy = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copy[j][n-1-i] = a[i][j]
    return copy
for t_case in range(T):
    N, S = input().split()
    N = int(N)
    board = []
    tmp = []
    res = []
    for i in range(N):
        board.append(list(map(int, input().split())))
    board = rotate(board)
    for i in range(N):
        tmp.append(board[i].pop())
        if board[i].pop() == tmp[-1]:
            tmp.clear()
            res.append(board[i] * 2)
            


