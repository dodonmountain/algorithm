import sys;sys.stdin=open('input.txt')


def solve(s, d, ops):
    global mx, mn
    if d == N:
        if s < mn:mn = s
        if s > mx:mx = s
        return
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            if i == 0:
                solve(s + arr[d], d + 1, ops)
            elif i == 1:
                solve(s - arr[d], d + 1, ops)
            elif i == 2:
                solve(s * arr[d], d + 1, ops)
            elif i == 3:
                solve(int(s / arr[d]), d + 1, ops)
            ops[i] += 1

# main()
T = int(input())
for t_case in range(T):
    N = int(input())
    ops = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    mx, mn = -9999999999, 0x999999999
    solve(arr[0], 1, ops)
    print('#{} {}'.format(t_case+1, mx-mn))