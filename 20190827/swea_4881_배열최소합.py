import sys
sys.stdin = open("input4881.txt")
from itertools import product,permutations
T = int(input())

def adv(y, N, tmp):
    global mintmp
    if y == N:
        if tmp < mintmp:
            mintmp = tmp
        return
    if tmp > mintmp:
        return
    for i in range(N):
        if checker[i]:
            continue
        tmp += arr[y][i]
        checker[i] = True
        adv(y+1, N, tmp)
        tmp -= arr[y][i]
        checker[i] = False



for t_case in range(T):
    N = int(input())
    checker = [False] * N
    arr = []
    mintmp = 987654321
    for numbers in range(N):
        arr.append(list(map(int, input().split())))
    adv(0,N,0)
    print('#{} {}'.format(t_case+1, mintmp))



    # print("#{} {}".format(t_case+1, min(res)))