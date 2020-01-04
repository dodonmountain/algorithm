import sys
sys.stdin = open('1493.txt')

T = int(input())

board = []
arr = []
k = 1
for l in range(500):
    arr = []
    for i in range(500):
        arr.append(i+k)
        k += 1 + i + l
    board.append(arr)
    k = board[-1][0] + l + 1
for t_case in range(T):
    p, q = map(int, input().split())
    a,b,c,d = 0,0,0,0
    for i in range(500):
        for j in range(500):
            if a and b and c and d:
                break
            if board[j][i] == p:
                a, b = j+1, i+1
            if board[j][i] == q:
                c, d = j+1, i+1
    res = board[a+c-1][b+d-1] 
    print('#{} {}'.format(t_case+1, res))
    
    