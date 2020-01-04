import sys; sys.stdin = open('수영장.txt')


def solve(s, d):
    global tmp
    if d == 12:
        if s < tmp:
            tmp = s
        return
    solve(s + price[0] * plan[d], d + 1)
    solve(s + price[1], d + 1)
    if d < 10:
        solve(s + price[2], d + 3)

T = int(input())

for t_case in range(T):
    price = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    tmp = 0x999999999
    solve(0, 0)
    if tmp > price[3]:
        tmp = price[3]
    print('#{} {}'.format(t_case+1, tmp))