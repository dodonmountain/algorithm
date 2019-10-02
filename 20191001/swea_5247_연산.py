import sys; sys.stdin = open('5247.txt')
from time import time
s_t =time()


def bfs():
    q = []
    q.append((M,0))
    visit = set()
    w = 0
    while q:
        here, d = q[w]
        if here == N:
            return d
        cal = [here >> 1, here+1, here-1,  here + 10]
        for i in range(4):
            if i == 0 and here & 1:continue
            if cal[i] not in visit and 0 < cal[i] < 1000001:
                q.append((cal[i], d + 1))
                visit.add(cal[i])
        w += 1
        
for t_case in range(int(input())):
    N, M = map(int, input().split())
    print('#{} {}'.format(t_case+1, bfs()))

print(time() - s_t)
