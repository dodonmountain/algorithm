import sys
from pprint import pprint
sys.stdin = open("input.txt")

from collections import deque

T = int(input())

for t_case in range(T):
    lst = []
    
    V, E = map(int, input().split())
    graph = {x:[] for x in range(1,V+1)}
    # 입력 받기 + 초기화
    for nods in range(E):
        lst += [list(map(int, input().split()))]
    S, G = map(int, input().split())
    # S 시작 G 도착
    #  받은 리스트를 그래프 형식의 딕셔너리로 변환
    for i in range(len(lst)):
        graph[lst[i][0]] += [lst[i][1]]
    # print('>>>>>>>>>>>>>>>>>>>>>>>>>>>그래프<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
    # pprint(graph,indent=2,width=20)
    # dfs 구현
    def dfs(start, graph):
        visited = deque()
        # 이미 방문한 노드
        stack = deque()
        # 지금부터 갈 노드
        stack.append(start)
        # 스택이 비어있지 않으면 = > 스택이 비면 모두 방문했으므로 탐색 종료
        while stack:
            here = stack.pop()
            # 후입 선출
            if here not in visited:
                # 현재 위치를 방문 기록에 저장하고
                visited.append(here)
                # 스택에 여기서부터 갈 수 있는 노드를 저장한다.
                stack.extend(graph[here])
        return visited
    # print('시작점:',S,'목표지점',G)
    # print('DFS결과:',dfs(S, graph))
    # print('경로 존재여부:',G in dfs(S, graph))
    # print('=============================================================')
    if G in dfs(S, graph):
        print('#{} {}'.format(t_case + 1, 1))
    else:
        print('#{} {}'.format(t_case + 1, 0))

