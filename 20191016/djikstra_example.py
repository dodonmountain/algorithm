V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))


def djikstra(s):
    D = [0xfffffffff] * (V+1) # D[] 초기값 설정
    cnt = V
    while cnt:
        # 아직 선택되지 않는 노드 중에 D[node]가 최소인 정점을 찾는다. 
        for v, w in G[u]:
            if D[v] > D[u] + w:
                D[v] = D[u] + w
        cnt -= 1