import sys;sys.stdin = open('boj10845.txt')

from collections import deque
import sys
input = sys.stdin.readlines
rawinput = input()
N = int(rawinput[0])
q = deque()
for i in range(1, N + 1):
    com = rawinput[i].rstrip('\n')
    try:
        com, num = com.split()
    except:
        pass
    if com == 'push':
        q.append(num)
    elif com == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif com == "size":
        print(len(q))
    elif com == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif com == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif com == "back":
        if q:
            print(q[-1])
        else:
            print(-1)
