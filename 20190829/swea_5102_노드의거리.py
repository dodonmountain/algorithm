import sys
sys.stdin = open("5102.txt")

from collections import deque
def bfs(s,g):
    Q = deque()
    visit = [0] * (V + 1)
    Q.append(s)
    while Q:
        v = Q.popleft()
        for w in graph[v]:
            if not visit[w]:
                visit[w] = True
                Q.append(w)
                D[w] = D[v] + 1
    return D[g]

T = int(input())
for t_case in range(T):
    V, E = map(int, input().split())
    graph = {x:[] for x in range(1,V + 1)}
    tmp = []
    D = [0] * (V + 1)
    for _ in range(E):
        tmp.extend(list(map(int, input().split())))
    for i in range(0, len(tmp),2):
        graph[tmp[i]].append(tmp[i+1])
    S, G = map(int, input().split())
    print(graph)
    print("#{} {}".format(t_case+1, bfs(S,G)))
