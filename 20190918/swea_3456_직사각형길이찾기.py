import sys
sys.stdin = open('3456.txt')

T = int(input())

for t_case in range(T):
    arr = list(map(int, input().split()))
    a = arr.pop()
    if arr[0] == a:
        res = arr[1]
    else:
        if arr[1] == a:
            res = arr[0]
        else:
            res = a
    print('#{} {}'.format(t_case+1, res))