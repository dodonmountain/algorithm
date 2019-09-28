def solve(s,d):
    global cnt
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
cnt = 0
solve([],0)

