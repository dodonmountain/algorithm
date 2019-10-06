import sys;sys.stdin=open('1258.txt')
delta = ((0,1),(1,0),(-1,0),(0,-1))
from collections import deque
def bfs(s):
    q = deque();q.append(s)
    visit[s[0]][s[1]] = 1
    h,w = 0,0
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx > n-1 or ny < 0 or ny > n - 1:continue
            if not visit[nx][ny] and board[nx][ny] != 0:
                visit[nx][ny] = 1
                q.append((nx, ny))
                if nx - s[0] + 1 > h:
                    h = nx - s[0] + 1
                if ny - s[1] + 1 > w:
                    w = ny - s[1] + 1
    return (h, w)
for t_case in range(int(input())):
    n = int(input());answer = []
    board = [list(map(int, input().split())) for _ in range(n)]
    visit = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] != 0 and not visit[i][j]:
                answer.append(bfs((i,j)))
    answer.sort(key=lambda x:(x[0]*x[1], x[0]))
    result = [len(answer)]
    for i in answer:
        result.append(i[0])
        result.append(i[1])
    print('#{}'.format(t_case+1), *result)