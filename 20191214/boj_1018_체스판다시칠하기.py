import sys;sys.stdin=open('chess.txt')

wboard = [['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W']]

bboard = [['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B'],
        ['B','W','B','W','B','W','B','W'],
        ['W','B','W','B','W','B','W','B']]

def check(x, y):
    wcount, bcount = 0, 0
    for i in range(8):
        for j in range(8):
            if board[x+i][y+j] != wboard[i][j]:
                wcount += 1
            if board[x+i][y+j] != bboard[i][j]:
                bcount += 1
    return min(wcount, bcount)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
minnow = check(0,0)
for i in range(N-7):
    for j in range(M-7):
        tmp = check(i, j)
        if check(i, j) < minnow:
            minnow = tmp 
print(minnow)