import sys
sys.stdin = open('5208.txt')

def solve(now, bt,cnt):
    global tmp
    if now == N-1:
        if tmp > cnt:
            tmp = cnt
        return
    if cnt >= tmp:
        return
    if bt <= 0 and now > 0:
        return
    if arr[now] >= N-1-now:
        solve(now+N-1-now, 1, cnt+1)
    else:
        solve(now+1, arr[now], cnt + 1)
        solve(now+1, bt - 1, cnt)


for t_case in range(int(input())):
    arr = list(map(int, input().split()))
    N = arr.pop(0)
    road = list(range(N))
    tmp = 9999999999999
    solve(0, 0, 0)
    print('#{} {}'.format(t_case+1, tmp-1))