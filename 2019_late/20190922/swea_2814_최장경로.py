import sys
sys.stdin = open('2814.txt')

def dfs(s,d):
    global tmp
    if d > tmp:
        tmp = d
    for w in G[s]:
        if not visit[w]:
            visit[w] = 1
            dfs(w,d+1)
            visit[w] = 0

for t_case in range(int(input())):
    n, m = map(int, input().split())
    G = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int, input().split())
        G[a] += [b]
        G[b] += [a]
    visit = [0] * (n+1)
    tmp = 0
    for i in range(1, n+1):
        visit[i] = 1
        dfs(i,0)
        visit[i] = 0
    print('#{} {}'.format(t_case+1, tmp+1))
    