import sys
sys.stdin = open("5099.txt")
from collections import deque

T = int(input())

for t_case in range(T):
    N, M = map(int, input().split())
    cheese = deque(map(int, input().split()))
    rot = 0
    k = 0
    oven, tmp = deque(), deque()
    for i in range(N):
        oven.append([cheese.popleft(),k])
        k += 1
    while len(oven) > 1:
        head = oven.popleft()
        head[0] = head[0] // 2
        if head[0] == 0:
            if cheese:
                oven.appendleft([cheese.popleft(),k])
                k+=1
        else:
            oven.append(head)
    print('#{} {}'.format(t_case+1, oven[0][1]+1))