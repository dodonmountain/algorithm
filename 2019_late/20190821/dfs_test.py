import sys
sys.stdin = open('input.txt')

V, E = map(int, input().split())
lst = []
graph = {x:[] for x in range(1,V+1)}
for nods in range(E):
    lst += [list(map(int, input().split()))]
for i in range(len(lst)):
    graph[lst[i][0]] += [lst[i][1]]
print(graph)

def dfs(start, graph):
    visited, stack = [], []
    stack.append(start)
    while stack:
        here = stack.pop()
        if here not in visited:
            visited.append(here)
            stack.extend(graph[here])
    return visited
print(dfs(1, graph))
visit = [False]*(V+1)
def dfs_recur(node):
    visit[node] = True
    print(node, end='')
    for sel in graph[node]:
        if not visit[node]:
            dfs_recur(sel)
print(dfs_recur(1))