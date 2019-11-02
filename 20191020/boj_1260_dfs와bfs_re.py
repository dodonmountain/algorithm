def dfs(s):
    visit[s] = 1
    print(s, end=' ')
    for w in G[s]:
        if not visit[w]:
            dfs(w)

def bfs(s):
    from collections import deque
    q = deque()
    q.append(s)
    bvisit = [0] * (v+1)
    bvisit[s] = 1
    print(s, end=' ')
    while q:
        here = q.popleft()
        for w in G[here]:
            if not bvisit[w]:
                bvisit[w] = 1
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
bfs(s)