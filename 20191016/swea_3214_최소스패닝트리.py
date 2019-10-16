import sys;sys.stdin = open('3214.txt')

def find(p):
    if parent[p] == p:return p
    parent[p] = find(parent[p])
    return parent[p]

for t_case in range(int(input())):
    V, E = map(int, input().split())
    Edge = [tuple(map(int, input().split())) for _ in range(E)] # (u, v, w)
    parent = [i for i in range(V+1)]
    answer = 0
    Edge.sort(key=lambda x:x[2]) # 가중치 오름차순 정렬
    MST = []
    idx = 0
    while len(MST) < V - 1: # V - 1 개의 간선을 선택
        u, v, w = Edge[idx]
        a, b = find(u), find(v)
        if a!= b:
            MST.append((u, v, w))
            parent[b] = a
        idx += 1
    for i in MST:
        answer += i[2]
    print('#{} {}'.format(t_case+1, answer))