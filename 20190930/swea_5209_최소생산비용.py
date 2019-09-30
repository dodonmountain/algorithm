import sys; sys.stdin = open('5209.txt')

def solve(s,d):
    global tmp
    if d == N:
        if s < tmp:
            tmp = s
        return
    if s >= tmp:
        return
    for i in range(N):
        if not used[i]:
            used[i] = 1
            solve(s + arr[d][i], d + 1)
            used[i] = 0


for t_case in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    used, tmp = [0] * (N+1), 0
    for i in range(N):
        tmp += arr[i][i]
    solve(0, 0)
    print('#{} {}'.format(t_case+1, tmp))