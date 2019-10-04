import math
T = int(input())

for t_case in range(T):
    n = int(input())
    arr = list(map(int, input().split()))
    ans = math.ceil(sum(arr) / n)
    print(ans)
