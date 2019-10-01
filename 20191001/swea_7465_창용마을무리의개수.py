import sys; sys.stdin = open('7465.txt')



def dfs(s):
    visit[s] = 1
    # print(s, end=' ')
    for w in G[s]:
        if not visit[w]:
            dfs(w)



T = int(input())

for t_case in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for i in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)
    visit = [0] * (N+1);cnt = 0
    for i in range(1, N + 1):
        if not visit[i]: 
            dfs(i)
            cnt += 1
    print('#{} {}'.format(t_case+1, cnt))