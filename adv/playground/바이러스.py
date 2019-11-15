N = int(input())
E = int(input())
G = [[] for _ in range(N+1)]
for i in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
from collections import deque
q = deque([1])
visit = [0] * (N+1)
while q:
    x = q.popleft()
    for w in G[x]:
        if not visit[w]:
            visit[w] = 1
            q.append(w)
print(sum(visit)-1)