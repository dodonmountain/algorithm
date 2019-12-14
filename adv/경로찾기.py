N = int(input())
G = [[] for _ in range(N)]
for i in range(N):
    adjlist = list(map(int, input().split()))
    for j in range(N):
        if adjlist[j]:
            G[i].append(j)
from collections import deque
q = deque()
q.append()