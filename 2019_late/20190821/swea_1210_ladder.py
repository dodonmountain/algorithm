import sys
sys.stdin = open("input.txt")
from pprint import pprint

def dfs(start, graph):
    visited, stack = [], []
    stack.append(start)
    while stack:
        here = stack.pop()
        if here not in visited:
            visited.append(here)
            stack.extend(graph[here])
    return visited

T = 10
for t_case in range(T):
    ladder = []
    lst = []
    __ = input()
    for _ in range (100):
        ladder.append(list(map(int, input().split())))
    for i in range(100):
        for j in range(100):
            if ladder[i][j] == 1:
                lst += [[i,j]]
            elif ladder[99][j] == 2:
                lst += [[i,j]]
                goal = j 
    k = 99
    while k > 1:
        # 한칸 올라가면서
        k -= 1
        for i in lst:
            if i[0] == k: # 높이가 같고
                if abs(i[1]-goal) < 2: # 접근가능하다면
                    goal = i[1]
    print(goal)
#     x = 98
#     direction = 1
#     while x > 0:
#         if direction == 1:
#             if ladder[x][y+1] == 1:
#                 if y < 99:
#                     y += 1
#                 else:
#                     direction = 0
#             else:
#                 direction = 0
#         elif direction == -1:
#             if ladder[x][y-1] == 1:
#                 if y > 0:
#                     y -= 1
#                 else:
#                     direction = 0
#             else:
#                 direction = 0
#         elif direction == 0:
#             x -= 1
#             if (ladder[x][y-1],ladder[x][y],ladder[x][y+1]) == (1,1,0):
#                 direction = -1
#             elif (ladder[x][y-1],ladder[x][y],ladder[x][y+1]) == (0,1,1):
#                 direction = 1
#     print('#{} {}'.format(t_case+1, y))


