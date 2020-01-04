import sys
sys.stdin = open('6057.txt')

T = int(input())
def dfs(s):
    stack = []
    visit = [0] * (N+1)
    stack.append(s)
    while stack:
        here = stack.pop()
        if not visit[here]:
            visit[here] = 1
            stack.extend(graph[here])
            print(here)
        

for t_case in range(T):
    N, M = map(int, input().split())
    graph = {x: [] for x in range(1,N+1)}
    for i in range(M):
        a, b  = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    dfs(1)
