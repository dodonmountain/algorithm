import sys
sys.stdin = open('5215.txt')


T = int(input())

for t_case in range(T):
    N, L = map(int, input().split())
    arr,res = [], []
    for i in range(N):
        arr.append(tuple(map(int, input().split())))
    for i in range(1 << N):
        tmp,tmp2 = [], []
        for j in range(N):
            if i & (1 << j):
                tmp.append(arr[j][1])
                tmp2.append(arr[j][0])
        if sum(tmp) <= L:
            res.append(sum(tmp2))
    print('#{} {}'.format(t_case+1, max(res)))