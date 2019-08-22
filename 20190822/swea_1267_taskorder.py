import sys
sys.stdin = open("input.txt")
from pprint import pprint
T = 1

for t_case in range(T):
    V, E = map(int, input().split())
    lines = list(map(int, input().split()))
    graph = { x:[] for x in range(1, V + 1)}
    graph2 = { x:[] for x in range(1, V + 1)}


    for i in range(len(lines)):
        if i % 2:
            graph[lines[i-1]] += [lines[i]]
            graph2[lines[i]] += [lines[i-1]]

    def dfs(start, graph):
        visited = []
        covered = []
        q = []
        q.append(start)
        while q:
            for nods in graph[q.pop()]:
                if nods not in visited and nods not in covered: # 발견도 방문도 안 한 경우 발견목록에 추가
                    covered.append(nods)
            for i in range(len(covered)):
                if graph2[covered[i]] == []:
                    visited.append(covered[i]) # 방문
                else:
                    q.append(graph2[covered[i]].pop()) # 큐에다가 조사 행렬 넣고 기다려보기         
        return visited
    
    startlist = []
    # for i in graph2.items():
    #     if i[1] == []:
    #         startlist.append(i[0])
    # startlist.sort()
    # result = []
    # for task in startlist:
    #     result.append(dfs(task, graph))
    # result.sort()
    print("#{} {}".format(t_case+1 , ' '.join(map(str, dfs(138, graph)))))
















# for t_case in range(T):
#     V, E = map(int, input().split())
#     lines = list(map(int, input().split()))
#     graph = { x:[] for x in range(1, V + 1)}
#     graph2 = { x:[] for x in range(1, V + 1)}
#     vs = []
    # for i in range(len(lines)):
    #     if i % 2:
    #         graph[lines[i-1]] += [lines[i]]
    #         vs.append(lines[i])
    #         graph[lines[i-1]]
#     for i in range(len(lines)):
#         if i % 2:
#             graph2[lines[i]] += [lines[i-1]]

#     visited, stack = [], []
#     for k in startlist:
#         stack.append(k)
#         while stack:
#             here = stack.pop()
#             if here not in visited:
#                 if graph2[here] != []:
#                     for i in range(1, len(graph2[here])+1):
#                         if graph2[i] in visited:
#                             graph2.pop(i)
#                     print('graph2',graph2, here)
#                     stack.extend(graph2[here])
#                 else:
#                     visited.append(here)
#                     stack.extend(graph[here])
#     print("#{} {}".format(t_case+1, ' '.join(map(str, visited))))
        

