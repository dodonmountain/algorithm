from itertools import combinations_with_replacement as cb
import sys
sys.stdin = open('dessert.txt')
delta = ((1, 1), (-1, 1), (-1, -1), (1, -1))


def dfs(s, size, sweets):
    global answer
    x, y = s
    for edge in range(4):
        dx, dy = delta[edge]
        if edge % 2 == 0:
            for _ in range(size[0]-1):
                x, y = x + dx, y + dy
                if x < 0 or y < 0 or x > N-1 or y > N-1:
                    return
                if board[x][y] in sweets:
                    return
                sweets.add(board[x][y])
        else:
            for _ in range(size[1]-1):
                x, y = x + dx, y + dy
                if x < 0 or y < 0 or x > N-1 or y > N-1:
                    return
                if board[x][y] in sweets:
                    return
                sweets.add(board[x][y])
    cnt = len(sweets)
    if cnt > answer:
        answer = cnt


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    sizes = list(cb(range(2, N), 2))
    sizes.pop()
    for i in range(len(sizes)-1, -1, -1):
        one, two = sizes[i]
        if one != two:
            sizes.append((two, one))
    sizes.sort(reverse=True)
    answer = -1
    for i in range(N):
        for j in range(N):
            for size in sizes:
                dfs((i, j), size, set())
    print('#{} {}'.format(tc, answer))
