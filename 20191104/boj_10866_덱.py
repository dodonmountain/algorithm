import sys; sys.stdin=open('d.txt')
input = sys.stdin.readline
from collections import deque

q = deque()
n = int(input())
for i in range(n):
    a = input().strip()
    if a[-1].isdecimal():
        query, x = a.split()
    else:
        query = a
    if query == 'push_front':
        q.appendleft(x)
    elif query == 'push_back':
        q.append(x)
    elif query == 'pop_front':
        if q: print(q.popleft())
        else: print(-1),
    elif query == 'pop_back':
        if q: print(q.pop())
        else: print(-1),
    elif query == 'size':
        print(len(q))
    elif query == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif query == 'front':
        if q: print(q[0])
        else: print(-1)
    elif query == 'back':
        if q: print(q[-1])
        else: print(-1)

