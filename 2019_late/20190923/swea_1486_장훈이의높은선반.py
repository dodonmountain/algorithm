import sys
sys.stdin = open('1486.txt')
def solve(s, d):
    global tmp
    if s >= b:
        if abs(b - s) < abs(b-tmp):
            tmp = s
        return
    if d == n:
        return
    solve(arr[d] + s, d + 1)
    solve(s, d + 1)

for t_case in range(int(input())):
    n, b = map(int, input().split())
    arr = list(map(int, input().split()))
    tmp = 0
    for i in range(n):
        solve(0, i)
    print('#{} {}'.format(t_case+1, abs(b-tmp)))