import sys
sys.stdin = open("input.txt")

T = int(input())

for t_case in range(T):
    N = int(input())
    lst = list(range(N))
    syn = []
    B = []
    C = []
    for _ in range(N):
        syn.append(list(map(int, input().split())))
    for i in range(1 << N):
        A = []
        for j in range(N + 1):
            if i & (1 << j):
                A.append(lst[j])
        if len(A) == 2:
            B.append(A)
    for i in range(len(B)):
        a, b = B[i][0], B[i][1]
        C.append(syn[a][b] + syn[b][a])
    C.sort()
    tmp = 9876543211
    for num in range(len(C)-1):
        if abs(C[num] - C[num+1]) <= tmp:
            tmp = C[num] - C[num+1]
    print(C)
    print(abs(tmp))






