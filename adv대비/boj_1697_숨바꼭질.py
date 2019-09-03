import sys
sys.stdin = open('1697.txt')
from collections import deque
N, K = map(int, input().split())
def bfs(s):
    q = deque()
    visit = [0] * 100001
    D = [0] * 100001
    q.append(s)
    while q:
        here = q.popleft()
        graph = []
        if 0 < here*2 < 100001:
            graph.append(here * 2)
        if 0 <= here - 1 < 100001:
            graph.append(here - 1)
        if 0 <= here + 1 < 100001:
            graph.append(here + 1)
        for w in graph:
            if visit[w] == 0:
                visit[w] = 1 
                D[w] = D[here] + 1
                q.append(w)
    return D[K]
if N != K:
    print(bfs(N))
else:
    print(0)
