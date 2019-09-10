import sys
sys.stdin = open('2007.txt')
from collections import deque

T = int(input())

for t_case in range(T):
    left,right = deque(), deque()
    arr = deque(input())
    cnt = 0
    checker = 2
    while arr:
        for i in range(checker):
            left.appendleft(arr.pop())
        for i in range(checker):
            right.appendleft(arr.pop())
        if left == right:
            break
        else:
            arr.extend(right)
            arr.extend(left)
            left.clear()
            right.clear()
            checker += 1
    print('#{} {}'.format(t_case+1 ,checker))

