N = int(input())

def solve(s,d):
    global tmp
    if d > 1:
        if d > tmp:
            return
    if s == 1:
        if d < tmp:
            tmp = d
        return
    if not s % 3:
        solve(s//3, d+1)
    if not 1 & s:
        solve(s//2, d+1)
    solve(s-1, d+1)
tmp = 9999999999
solve(N, 0)
print(tmp)