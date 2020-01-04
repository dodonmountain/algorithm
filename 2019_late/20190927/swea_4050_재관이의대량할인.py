import sys; sys.stdin = open('4050.txt')
from collections import deque
for t_case in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort();arr = deque(arr)
    res = 0
    while arr:
        if len(arr) > 2:
            arr.pop()
            res += arr.popleft()
            res += arr.popleft()
        else:
            res += sum(arr)
            break
    print(arr)
    print(res)