import sys
sys.stdin = open("1238.txt")

import operator
from collections import deque
def bfs(s):
    Q = deque()
    depth = [0] * 101
    res, qres = [], []
    visit = [0] * 101
    Q.append(s)
    while Q:
        v = Q.popleft()
        for w in graph[v]:
            if not visit[w]:
                visit[w] = True
                Q.append(w)
                depth[w] = depth[v] + 1
    for i in range(1, len(depth)):
        if depth[i] == max(depth):
            res.append(i)
    return max(res)


T = 10
for t_case in range(T):
    E, S = map(int, input().split())
    tmp = []
    tmp = list(map(int, input().split()))
    graph = {}
    DD = []
    for i in range(E):
        graph[tmp[i]] = []
    for i in range(0, E, 2):
        if tmp[i+1] not in graph[tmp[i]]:
            graph[tmp[i]].append(tmp[i+1])
    V = len(graph)
    D = [0] * 101
    print('#{} {}'.format(t_case+1, bfs(S)))

