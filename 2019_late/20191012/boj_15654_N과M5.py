import sys;sys.stdin = open('15654.txt')

def solve(s, d):
    if len(s) == m:
        print(*s)
        return
    if d == n:
        return
    solve(s + [arr[d]], d + 1)
    solve(s, d + 1)

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
solve([], 0)