import sys;sys.stdin = open('2660.txt')

from collections import deque

def bfs(s):
    q = deque();q.append(s)
    visit = [0] * (N + 1);visit[s] = 1
    while q:
        here = q.popleft()
        for w in G[here]:
            if not visit[w]:
                visit[w] = 1
                q.append(w)
                D[w] = D[here] + 1


N = int(input()) 
G = [[] for _ in range(N + 1)]
while True:
    a, b = map(int, input().split())
    if (a, b) == (-1, -1):
        break
    G[a].append(b);G[b].append(a)
result = []
minnow = 0x9999999
for i in range(1, N + 1):
    D = [0] * (N+1)
    bfs(i)
    md = max(D)
    if md <= minnow:
        if md == minnow:
            result.append(i)
        else:
            result = []
            minnow = md
            result.append(i)
print(minnow, len(result))
print(*result)
