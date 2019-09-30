import sys; sys.stdin = open('5247.txt')

from collections import deque

def bfs():
    global N, M, result
    while q:
        smthing = q.pop()
        if N == M:
            answer = tmp
            return
        for i in range(4):
            if i == 0:
                if 0 <= tmp < 1000001:
                    Q.append()
                    pass
            elif i == 1:
                if 0 <= tmp < 1000001:
                    Q.append()
                    pass
            elif i == 2:
                if 0 <= tmp < 1000001:
                    Q.append()
                    pass
            elif i == 3:
                if 0 <= tmp < 1000001:
                    Q.append()
                    pass

for t_case in range(int(input())):
    N, M = map(int, input().split())
    result = 0
    bfs()
    print(result)
