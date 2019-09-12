import sys
sys.stdin = open('1959.txt')

T = int(input())

for t_case in range(T):
    N, M = map(int, input().split())
    arrA = list(map(int, input().split()))
    arrB = list(map(int, input().split()))
    if N > M:
        short = arrB
        long = arrA
    else:
        short = arrA
        long = arrB
    diff = abs(N - M)
    res = []
    for j in range(diff+1):
        tmp = 0
        for i in range(len(short)):
            tmp += short[i] * long[i+j]
        res.append(tmp)
    print('#{} {}'.format(t_case+1, max(res)))