def solve(s):
    if len(s) == m:
        print(*s)
        return
    for i in range(n):
        if arr[i] not in visit:
            visit.add(arr[i])
            s.append(arr[i])
            solve(s)
            s.pop()
            visit.remove(arr[i])
        


n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
visit = set()
solve([])