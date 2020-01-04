L, P = map(int, input().split())
arr = list(map(int, input().split()))
ans = L * P
res = []
for i in arr:
    res.append(i-ans)
print(*res)