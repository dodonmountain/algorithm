import sys
sys.stdin = open('2748.txt')

def dp_fib(n):
    if memo[n] != 0:
        return memo[n]
    if n < 3:
        return 1
    else:
        memo[n] = dp_fib(n-1) + dp_fib(n-2)
        return memo[n]

memo = [1,1] + [0] * 100
print(dp_fib(int(input())))
    