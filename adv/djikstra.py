import sys; sys.stdin = open('weighted_graph.txt')

from queue import PriorityQueue

def DIJKSTRA_PRIORITYQ(s):

    D = [0xffffff] * (V + 1)
    P = [i for i in range(V + 1)]
    visit = [False] * (V + 1)
    D[s] = 0
    Q = PriorityQueue()
    Q.put((0, s))

    while not Q.empty():
        d, u = Q.get()
        if d > D[u]: continue

        visit[u] = True
        for v, w in G[u]:
            if not visit[v] and D[v] > D[u] + w:
                D[v] = D[u] + w
                P[v] = u
                Q.put((D[v], v))
    for i in D[1:V + 1]:
        if i == 0xffffff:
            print('INF')
        else:
            print(i)


V, E = map(int, input().split())
S = int(input())
G = [[] for _ in range(V + 1)]
for i in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

DIJKSTRA_PRIORITYQ(S)
