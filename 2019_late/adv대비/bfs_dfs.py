from collections import deque

def dfs(start):

    visit[start] = 1
    result1.append(start)
    for w in G[start]:
        if not visit[w]:
            dfs(w)

def bfs(start):
    visit[start] = 1
    queue = deque()
    queue.append(start)
    result2.append(start)
    while queue:
        q = queue.popleft()
        for w in G[q]:
            if not visit[w]:
                visit[w] =1
                queue.append(w)
                result2.append(w)



N, M, V = map(int, input().split())
visit = [0]*(N+1)
G = [[] for _ in range(N+1)]
for _ in range(M):
    u,v = map(int,input().split())
    G[u].append(v)
    G[v].append(u)
for i in range(len(G)):
    G[i].sort()
result1,result2 = [], []
dfs(V)