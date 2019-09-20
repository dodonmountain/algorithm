import sys
sys.stdin = open('1865.txt')

def solve(d,ss):
    global tmp
    if d == N:
        if ss * 100 > tmp:
            tmp = ss * 100
        return
    if ss * 100 <= tmp:
        return
    for i in range(N):
        if used[i]:
            continue
        used[i] = 1
        solve(d+1,ss*(board[d][i]/100))
        used[i] = 0

for t_case in range(int(input())):
    N = int(input())
    used,tmp = [0]*N, 0
    board = [list(map(int, input().split())) for _ in range(N)]
    solve(0,1)
    print('#{} {:.6f}'.format(t_case + 1, round(tmp, 6)))



