from collections import deque
import sys;sys.stdin = open('boj10845.txt')


N = int(input())
q = deque()
for i in range(N):
    com = input()
    try:
        com, num = com.split()
    except:
        pass
    if com == 'push':
        q.append(num)
    elif com == "pop":
        try:
            print(q.popleft())
        except:
            print(-1)
    elif com == "size":
        print(len(q))
    elif com == "empty":
        if q:
            print(0)
        else:
            print(1)
    elif com == "front":
        try:
            print(q[0])
        except:
            print(-1)
    elif com == "back":
        try:
            print(q[-1])
        except:
            print(-1)
