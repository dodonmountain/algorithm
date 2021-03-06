def dfs(s):
    visit[s] = 1
    print(s, end=' ')
    for w in G[s]:
        if not visit[w]:
            dfs(w)
from collections import deque
def bfs(s):
    q= deque();q.append(s)
    visit[s] = 1
    print(s, end=' ')
    while q:
        here = q.popleft()
        for w in G[here]:
            if not visit[w]:
                visit[w] = 1
                q.append(w)
                print(w, end=' ')

v, e, s = map(int, input().split())
G = [[] for _ in range(v+1)]
for i in range(e):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
for i in G:
    i.sort()
visit = [0] * (v+1)
dfs(s)
print()
visit = [0] * (v+1)
bfs(s)