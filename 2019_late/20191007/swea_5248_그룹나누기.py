import sys;sys.stdin = open('5248.txt')

def uni(p, q):
    p = find(p)
    q = find(q)
    if p == q:return
    parent[q] = p

def find(p):
    if parent[p] == p:
        return p
    parent[p] = find(parent[p])
    return parent[p]

for t_case in range(int(input())):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    parent = [i for i in range(N + 1)]
    for i in range(M):
        if not i & 1:
            uni(arr[i], arr[i+1])
    for i in range(1, N+1):
        print(find(i))