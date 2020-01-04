import sys
sys.stdin = open('5603.txt')

T = int(input())

for t_case in range(T):
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    target = sum(arr)//N
    res = 0
    for i in arr:
        if i > target:
            res += i - target
    print('#{} {}'.format(t_case+1, res))