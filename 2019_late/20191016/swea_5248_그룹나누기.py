import sys;sys.stdin=open('5248.txt')

def uni(p, q):
    p = find(p)
    q = find(q)
    if p == q:return
    parent[q] = p

def find(p):
    if parent[p] == p:return p
    parent[p] = find(parent[p])
    return parent[p]

for t_case in range(int(input())):
    n, m = map(int, input().split())
    cnt, cmp = 0, set()
    parent = [i for i in range(n+1)]
    arr = list(map(int, input().split()))
    for i in range(0, m * 2, 2):
        if not i & 1:
            uni(arr[i], arr[i+1])
    for i in range(1, n+1):
        tmp = find(i)
        if tmp not in cmp:
            cnt += 1
            cmp.add(tmp)
    print('#{} {}'.format(t_case+1, cnt))

