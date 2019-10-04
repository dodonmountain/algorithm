import sys;sys.stdin = open('1325.txt')


import sys
input = sys.stdin.readline
from collections import deque

def bfs(s):
    D = 0
    q = deque()
    q.append(s)
    visit = [0] * (N + 1)
    visit[s] = 1
    while q:
        here = q.popleft()
        D += 1
        for w in G[here]:
            if not visit[w]:
                visit[w] = 1
                q.append(w)
    return D
                
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    G[b].append(a)
mxd = 0
result = []
for i in range(1, N + 1):
    if G[i]:
        tmp = bfs(i)
        if mxd <= tmp:
            if mxd < tmp:
                result = []
            mxd = tmp
            result.append(i)
print(*result)
