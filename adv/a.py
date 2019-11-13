delta = ((1, 0), (0, 1), (-1, 0), (0, -1))

from collections import deque
def bfs(node):
    q = deque()
    q.append(node)
    visit = [[0] * N for _ in range(N)]
    visit[s[0]][s[1]] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in delta:
            nx, ny = x + dx, y + dy
            if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
                continue
            if not visit[nx][ny]:
                visit[nx][ny]
                q.append((nx, ny))

def dfs(node):
    x, y = node
    visit[x][y] = 1
    for dx, dy in delta:
        nx, ny = x + dy, y + dy
        if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:continue
        if not visit[nx][ny]:
            dfs((nx,ny))
