import sys; sys.stdin = open('3752.txt')

from collections import deque

for t_case in range(int(input())):
    N = int(input())
    q = deque(sorted(map(int, input().split())))
    _max = sum(q)
    visit = [0] * 10000; visit[0] = 1
    while q:
        now = q.popleft()
        for i in range(_max-1, -1, -1):
            if visit[i]:
                visit[i + now] = 1
    print('#{} {}'.format(t_case+1, sum(visit)))