import sys
sys.stdin = open('11724.txt')

V, E = map(int, input().split())
graph = []
grp = {x:[] for x in range(1, V + 1)}
for _ in range(E):
    graph.append(list(map(int, input().split())))
for i in range(E):
    grp[graph[i][0]] += [graph[i][1]]
    grp[graph[i][1]] += [graph[i][0]]
res = set()
cnt = 0
def dfs(s):
    stack = []
    global res
    visit = [0] * (V + 1)
    stack.append(s)
    while stack:
        here = stack.pop()
        if visit[here] == 0:
            visit[here] = 1
            stack.extend(grp[here][::-1])
            res.add(here)
    return
for i in range(1, V + 1):
    if i in res:
        continue
    else:
        dfs(i)
        cnt += 1
print(cnt)

