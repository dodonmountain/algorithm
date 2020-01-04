import sys;sys.stdin = open('2644.txt')

from collections import deque

def bfs(s):
    q = deque();q.append(s)
    visit[s] = 0
    while q:
        here = q.popleft()
        for w in G[here]:
            if visit[w] == -1:
                visit[w] = visit[here] + 1
                if w == goal:
                    flag = True
                    return visit[w]
                q.append(w)
    return -1

n = int(input())
start, goal = map(int, input().split())
E = int(input())
G = [[] for _ in range(n+1)]
for i in range(E):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visit= [-1] * (n+1)
answer = bfs(start)
print(answer)
