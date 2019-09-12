import sys
sys.stdin = open("1961.txt")

from pprint import pprint

T = int(input())
for t_case in range(T):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    stack = []
    for i in range(N):
        tmp = ''
        for j in range(N-1,-1,-1):
            tmp += str(board[j][i])
        stack.append(tmp)
    for i in range(N-1,-1,-1):
        tmp = ''
        for j in range(N-1,-1,-1):
            tmp += str(board[i][j])
        stack.append(tmp)
    for i in range(N-1,-1,-1):
        tmp = ''
        for j in range(N):
            tmp += str(board[j][i])
        stack.append(tmp)
    print('#{}'.format(t_case+1))
    for i in range(N):
        print(stack[i],stack[i+N],stack[i+N+N])
