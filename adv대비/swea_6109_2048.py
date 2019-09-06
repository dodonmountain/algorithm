import sys
sys.stdin = open('6109.txt')
from pprint import pprint

T = int(input())

def rotate(a):
    n = len(a)
    copy = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            copy[j][n-1-i] = a[i][j]
    return copy

def push(a):
    for i in range(N):
        for j in range(N):
            if a[i][j] == 0:
                a[i].insert(a[i].pop(j),0)
def add(a):
    for i in range(N):
        for j in range(N-1,0,-1):
            if a[i][j] ==a[i][j-1]:
                a[i][j] *= 2
                a[i].pop(j-1)
                a[i].insert(0,0)


for t_case in range(T):
    N, S = input().split()
    N = int(N)
    board = []
    tmp = []
    res = []
    for i in range(N):
        board.append(list(map(int, input().split())))
    if S == 'up':
        board = rotate(board)
        push(board)
        add(board)
        board = rotate(board)
        board = rotate(board)
        board = rotate(board)
    elif S == 'down':
        board = rotate(board)
        board = rotate(board)
        board = rotate(board)
        push(board)
        add(board)
        board = rotate(board)
    elif S == 'left':
        board = rotate(board)
        board = rotate(board)
        push(board)
        add(board)
        board = rotate(board)
        board = rotate(board)
    else:
        push(board)
        add(board)
    print('#{}'.format(t_case+1))
    for i in range(N):
        print(*board[i])
