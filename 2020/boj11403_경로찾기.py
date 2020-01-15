import sys;sys.stdin=open('boj11403.txt')

def bfs(s):
    from collections import deque
    q = deque()
    visit = [0] * n
    q.append(s)
    while q:
        here  = q.popleft()
        for w in G[here]:
            if not visit[w]:
                visit[w] = 1
                q.append(w)
    print(*visit)

n = int(input())
G = [[] for _ in range(n)]
for i in range(n):
    arr = list(map(int, input().split()))
    for w in range(n):
        if arr[w]:
            G[i].append(w)
for a in range(n):
    bfs(a)