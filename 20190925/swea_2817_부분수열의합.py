import sys
sys.stdin = open('2817.txt')


def solve(s, d):
    global tmp
    if d == N:
        if s == K:
            tmp += 1
        return
    solve(s + arr[d], d + 1)
    solve(s, d + 1)

for t_case in range(int(input())):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    tmp = 0
    solve(0, 0)
    print('#{} {}'.format(t_case+1, tmp))
    
