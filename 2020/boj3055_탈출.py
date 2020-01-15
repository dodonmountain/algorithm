import sys;sys.stdin=open('boj3055.txt')


def bfs(s):
    from collections import deque
    q = deque()
    visit = [[0] * c for _ in range(r)]
    q.append(s[0], s[1])


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
