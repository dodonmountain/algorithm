import sys;sys.stdin=open('1248.txt')

def find_depth(node):
    stack = []
    stack.append(1)
    depth = [0] * (v+1)
    while stack:
        w = stack.pop()
        if w == node:
            return depth[w]
        for i in T[w]:
            stack.append(i)
            depth[i] = depth[w] + 1

def dfs(w):
    visit[w] = 1
    for s in T[w]:
        if not visit[s]:
            dfs(s)


for t_case in range(int(input())):
    v, e, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    P = [0] * (v+1)
    T = [[] for _ in range(v+1)]
    visit = [0] * (v+1)
    for i in range(0, 2 * e, 2):
        P[arr[i+1]] = arr[i]
        T[arr[i]].append(arr[i+1])
    da, db = find_depth(a), find_depth(b)
    while P[a] != P[b]:
        if da > db:
            P[a] = P[P[a]]
            da -= 1
        else:
            P[b] = P[P[b]]
            db -= 1
    lca = P[a]
    dfs(P[a])
    print('#{} {} {}'.format(t_case+1, lca, sum(visit)))
 