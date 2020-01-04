import sys
sys.stdin = open('1225.txt')

from collections import deque
T = 10

for t_case in range(T):
    trash = input()
    arr = deque(map(int, input().split()))
    i = 0
    while True:
        k = i % 5 + 1
        if arr[0] - k > 0:
            arr[0] -= k
            arr.rotate(-1)
            i += 1
        else:
            arr[0] = 0
            arr.rotate(-1)
            break
    print('#{}'.format(t_case+1), *arr)