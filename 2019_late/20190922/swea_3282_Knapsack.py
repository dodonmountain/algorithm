import sys
sys.stdin = open('3282.txt')

def dp_solve(n, space):
    if memo[n][space] != -1:
        return memo[n][space]
    if n == 0 or space == 0:
        return 0
    if arr[n][0] > space:
        return dp_solve(n-1, space)
    select = arr[n][1] + dp_solve(n - 1, space - arr[n][0])
    unselect = dp_solve(n - 1, space)
    if select > unselect:
        memo[n][space] = select
        return select
    else:
        memo[n][space] = unselect
        return unselect

for t_case in range(int(input())):
    N, k = map(int, input().split())
    arr = [0] + [list(map(int, input().split())) for _ in range(N)]
    memo = [[-1] * (k+1) for _ in range(N+1)]
    res = dp_solve(N, k)
    print('#{} {}'.format(t_case+1, res))
    