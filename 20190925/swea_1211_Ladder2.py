import sys; sys.stdin = open('1211.txt')
from pprint import pprint

dy = [-1, 0, 1]
def dfs(x, y):
    global tmp, res
    visit[x][y] = 1 # 방문 표시
    if x == 99:
        if sum(map(sum, visit)) < tmp:
            tmp = sum(map(sum, visit))
        return
    # 오른쪽으로 갈 수 있나?
    flag = 'down'
    if y + 1 < 100:
        if board[x][y + 1] == 1:
                flag = 'right'
    elif 0 <= y - 1:
        if board[x][y - 1] == 1:
                flag = 'left'

    if flag == 'right' and visit[x][y+1]==0:
        dfs(x, y + 1) # right
    elif flag == 'left' and visit[x][y-1]==0:
        dfs(x, y - 1) # left
    else:
        dfs(x + 1, y) # down



for __ in range(1):
    t_case = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    tmp = 999999999; res = 9999999999
    s_list = []
    for i in range(100):
        if board[0][i] == 1:
            s_list.append(i)
    print(s_list)
    for i in s_list:
        visit = [[0] * 100 for _ in range(100)]
        dfs(0, i)
    pprint(visit,width=1000)
