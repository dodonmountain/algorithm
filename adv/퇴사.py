import sys
sys.stdin = open('퇴사.txt')


def solve(d: int, money: int):
    global maxnow
    if d >= L:
        if money > maxnow:
            maxnow = money
        return
    if d + arr[d][0] <= L:
        solve(d+arr[d][0], money + arr[d][1])
    solve(d+1, money)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
L = len(arr)
maxnow = -1
solve(0, 0)
print(maxnow)
