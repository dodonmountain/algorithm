import sys
sys.stdin = open('키순서.txt')

def dfs(s, graph):
    global TempSet
    visit[s] = 1
    TempSet.add(s)
    for w in graph[s]:
        if visit[w] == [-1]:
            dfs(w, graph)


T = int(input())

for tc in range(T):
    N = int(input())
    M = int(input())
    G = [[] for _ in range(N+1)]
    RG = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        RG[b].append(a)
    cnt = 0
    for i in range(1, N+1):
        visit = [[-1] for _ in range(N+1)]
        TempSet = set()
        dfs(i,G)
        bigger = TempSet
        TempSet = set()
        dfs(i,RG)
        smaller = TempSet
        if len(bigger | smaller) == N:
            cnt += 1
    print('#{} {}'.format(tc+1,cnt))