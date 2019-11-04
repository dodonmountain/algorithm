def fib(n):
    if memo[n] != -1:
        return memo[n]
    memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

memo = [-1] * 46
memo[0] = 0
memo[1] = 1
memo[2] = 1
n = int(input())
print(fib(n))