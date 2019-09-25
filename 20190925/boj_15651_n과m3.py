def solve(s,d):
    if len(s) == m:
        print(*s)
        return
    for i in range(1, n+1):
        s.append(i)
        solve(s, d+1)
        s.pop()

n, m = map(int, input().split())
arr = list(range(1, n+1))
used = [0] * (n+1)
solve([],0)
