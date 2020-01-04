import sys
sys.stdin = open('1260.txt')
import collections

v_num, e_num, start = map(int, input().split())
edges = [[] for _ in range(v_num + 1)]
visited = [True] + [False] * v_num
for _ in range(e_num):
    v1, v2 = map(int, input().split())
    edges[v1].append(v2)
    edges[v2].append(v1)
for i in range(1, v_num + 1):
    edges[i].sort()
print(edges)

result = []
now = start
s = [now]
visited[now] = True
result.append(now)
while s:
    now = s.pop()
    for v in edges[now]:
        if not visited[v]:
            now = v
            visited[v] = True
            s.append(v)
            result.append(v)

print(' '.join(map(str, result)))
now = start
visited = [False] * (v_num + 1)
q = collections.deque()
result = [now]
q.append(now)
visited[now] = True
while q:
    now = q.popleft()
    for v in edges[now]:
        if not visited[v]:
            q.append(v)
            visited[v] = True
            result.append(v)
print(' '.join(map(str, result)))




