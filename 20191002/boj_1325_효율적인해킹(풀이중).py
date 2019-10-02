import sys;sys.stdin = open('1325.txt')


import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    global D
    q = deque()
    q.append(s)
    visit.add(s)
    while q:
        here = q.popleft()
        D += 1
        for w in G[here]:
            if w not in visit:
                visit.add(w)
                q.extend(G[w])
                
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    G[b].append(a)
mxd = 0
result = []
for i in range(1, N + 1):
    if G[i]:
        visit = set()
        D = 0
        bfs(i)
        if mxd <= D:
            mxd = D
            result.append((i, D))
print(*result)
