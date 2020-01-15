
N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
memo = [0] * (N+1)

for i in range(N - 1, -1, -1):
    if i + lst[i][0] <= N:
        memo[i] = max(memo[i + lst[i][0]] + lst[i][1], memo[i + 1])
print(memo[0])