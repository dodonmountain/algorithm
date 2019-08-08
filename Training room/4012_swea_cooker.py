import sys
sys.stdin = open("input.txt")

T = int(input())

for t_case in range(T):
    N = int(input())
    lst = list(range(N))
    syn = []
    B = []
    for _ in range(N):
        syn.append(list(map(int, input().split())))
    for i in range(1 << N):
        A = []
        for j in range(N + 1):
            if i & (1 << j):
                A.append(lst[j])
        if len(A) == 2:
            B.append(A)
    print(B)
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            else:
                print('S{}{} : {}'.format(i+1,j+1,syn[i][j] + syn[j][i]))




