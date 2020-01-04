import sys;sys.stdin = open('1265.txt')

for t_case in range(int(input())):
    N, P = map(int, input().split())
    arr = []
    tmp = N % P
    arr = [N // P]  * P
    if tmp:
        for i in range(tmp):
            arr[i] += 1
    res = 1
    for i in range(P):res *= arr[i]
    print('#{} {}'.format(t_case+1, res))