import sys
sys.stdin = open('1260.txt')

from collections import deque
V, E, S = map(int,input().split())
graph = []
for _ in range(E):
    graph.append(list(map(int, input().split())))
grp = {x:[] for x in range(1, V+1)}
for i in range(E):
    grp[graph[i][0]].extend([graph[i][1]])
    grp[graph[i][1]].extend([graph[i][0]])

for i in range(1, V+1):
    grp[i].sort()

def dfs(s):
    stack, res = [], []
    visit = [0] * (V + 1)
    stack.append(s)
    while stack:
        here = stack.pop()
        if visit[here] == 0:
            visit[here] = 1
            stack.extend(grp[here][::-1])
            res.append(str(here))
    return res

def bfs(s):
    q, res = deque(), []
    visit = [0] * (V + 1)
    q.append(s)
    res.append(str(s))
    visit[s] = 1
    while q:
        here = q.popleft()
        for w in grp[here]:
            if visit[w] == 0:
                visit[w] = 1
                q.append(w)
                res.append(str(w))
    return res

print(' '.join(dfs(S)))
print(' '.join(bfs(S)))

