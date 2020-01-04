n = int(input())
memo = [-1] * (n+1)
def solve(s):
    if memo[s] != -1:
        return memo[s]
    if s < 2:
        return 1
    memo[s] = solve(s-2) + solve(s-1)
    return memo[s]
print(solve(n)%10007)