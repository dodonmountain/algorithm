def solve(s, d):
    if d == M:
        print(*s)
        return
    mx = 1
    if s:
        mx = s[-1]
    for i in range(mx, N + 1):
        s.append(i)
        solve(s, d + 1)
        s.pop()

N, M = map(int, input().split())
solve([], 0)