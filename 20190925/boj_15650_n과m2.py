def solve(s,d):
    if len(s) == m:
        print(*s)
        return
    mxn = 1
    for j in range(len(used)-1,-1,-1):
        if used[j] != 0:
            mxn = j+1
            break
    for i in range(mxn, n+1):
        if not used[i]:
            s.append(i)
            used[i] =1
            solve(s, d+1)
            used[i] = 0
            s.pop()

n, m = map(int, input().split())
arr = list(range(1, n+1))
used = [0] * (n+1)
solve([],0)
