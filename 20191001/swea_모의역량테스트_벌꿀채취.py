import sys; sys.stdin = open('벌꿀채취.txt')
from pprint import pprint
from time import time
time = time()

def select(s, d, arr, sqr):
    global tmp
    if d == len(arr):
        if sqr > tmp:
            tmp = sqr
    else:
        if s + arr[d] <= C:
            select(s + arr[d], d + 1, arr, sqr + (arr[d]**2))
        select(s, d + 1, arr, sqr)



def catch(x, y):
    honey = []
    for i in range(M):
        honey.append(board[x][y+i])
    honey.sort(reverse=True)
    select(0, 0, honey, 0)
    return tmp

for t_case in range(int(input())):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0
    tmp = 0
    for i in range(N):
        for j in range(N-M+1):
            tmp = 0
            a = catch(i, j)
            for k in range(N):
                for l in range(N-M+1):
                    if k == i and l < j + M:
                        pass
                    else:
                        tmp = 0
                        b = catch(k, l)
                        if answer < a + b:
                            answer = a + b
    print('#{} {}'.format(t_case+1, answer))
