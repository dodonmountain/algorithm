import sys
sys.stdin = open('5642.txt')


for t_case in range(int(input())):
    N = int(input())
    arr = [-9999] + list(map(int, input().split()))
    memo = [-9999] * 100001
    for i in range(N+1):
        if memo[i - 1] + arr[i] > arr[i]:
            memo[i] = memo[i-1] + arr[i]
        else:
            memo[i] = arr[i]
    if max(memo) > max(arr):
        res = max(memo)
    else:
        res = max(arr)
    print('#{} {}'.format(t_case+1, res))