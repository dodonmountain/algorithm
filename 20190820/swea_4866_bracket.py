import sys
sys.stdin = open("input.txt")
import time
start = time.time()
from collections import deque

T = int(input())
for t_case in range(T):
    context = set('(){}')
    line = input()
    tmp = deque()
    for i in range(len(line)):
        if line[i] in context:        
            tmp.append(line[i])

    for _ in range(len(tmp)**2):
        if len(tmp) < 2:
            break
        elif tmp[0]+tmp[1] == '()' or tmp[0]+tmp[1] == '{}':
            print(tmp.popleft())
            print(tmp.popleft())
        else:
            tmp.rotate(-1)
        print(tmp)
    if tmp:
        print('#{} 0'.format(t_case+1))
    else:
        print('#{} 1'.format(t_case+1))
