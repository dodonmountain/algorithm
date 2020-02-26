def dfs(s):
    global visited, G, N, res
    for i in range(1, N+1):
        if G[s][i] and visited[i] == 0:
            visited[i] = 1
            res.add(i)
            dfs(i)
    return

N, M = map(int, input().split())
G = [[0] * (N+1) for _ in range(N+1)]
visited = [0] * (N+1)
cnt = 0
res = set()
for _ in range(M):
    u, v = map(int, input().split())
    G[u][v] = 1
    G[v][u] = 1

for i in range(1, N+1):
    if i not in res:
        visited[i] = 1
        cnt += 1
        dfs(i)

print(cnt)