import sys;sys.stdin = open('5521.txt')
from collections import deque
def bfs():
    q = deque()
    visit = [0] * (N+1) 
    D = [0] * (N+1)
    q.append(1)
    visit[1] = 1
    while q:
        here = q.popleft()
        for w in G[here]:
            if not visit[w]:
                visit[w] = 1
                q.append(w)
                D[w] = D[here] + 1
    cnt = 0
    for i in D:
        if 0 < i < 3:
            cnt += 1
    print('#{} {}'.format(t_case+1, cnt))

for t_case in range(int(input())):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    visit = [0] * (N+1)
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    bfs()

