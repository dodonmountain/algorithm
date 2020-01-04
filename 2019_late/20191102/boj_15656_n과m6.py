def solve(s):
    if len(s) == m:
        res = ''.join(map(str, s))
        if res not in visit:
            visit.add(res)
            print(*s)
        return
    for i in range(n):
        if s:
            if arr[i] >= s[-1]:
                s.append(arr[i])
                solve(s)
                s.pop()
        else:
            s.append(arr[i])
            solve(s)
            s.pop()


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
n = len(arr)
used = [0] * (n+1)
visit = set()
solve([])
