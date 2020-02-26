from math import factorial as f
n, k = map(int, input().split())
if k == 0:
    res = 1
else:
    res = f(n) // (f(k) * (f(n-k)))
print(res)