import sys; sys.stdin=open('9372.txt')
from collections import deque

T = int(input())

def bfs(s):
    q = deque()
    q.append(s)
    visit = [0] * (N + 1)
    visit[s] = 1
    D = [0] * (N + 1)
    while q:
        here = q.popleft()
        for w in G[here]:
            if not visit[w]:
                visit[w] = 1
                q.append(w)
                D[w] = D[here] + 1
    # print(sum(D))

        
for tc in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    for i in range(1, N+1):
        bfs(i)
    print(N-1)
