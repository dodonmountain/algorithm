import sys;sys.stdin = open('2531.txt')

from collections import deque
N, d, k, c = map(int, input().split())
q = deque([int(input()) for _ in range(N)])
visit = [0] * (d+1)
visit[c] = 1
maxnow = 0
for i in range(N):
    for j in range(k):
        visit[q[j]] = 1
    if sum(visit) > maxnow:
        maxnow = sum(visit)
    visit = [0] * (d+1)
    visit[c] = 1
    q.rotate(1)
print(maxnow)