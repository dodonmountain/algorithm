import sys
sys.stdin = open('6485.txt')

T = int(input())

for t_case in range(T):
    N = int(input())
    all = [0] * 5001
    for i in range(N):
        a, b = map(int, input().split())
        for i in range(a,b+1):
            all[i] += 1
    P = int(input())
    res = []
    for i in range(P):
        c = int(input())
        res.append(all[c])
    print('#{}'.format(t_case+1),*res)


