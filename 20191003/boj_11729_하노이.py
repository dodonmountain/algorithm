def solve(n,a,b,c):
    if n > 0:
        solve(n-1, a, c, b)
        print(f'{a} {c}')
        solve(n-1, c, b ,a)
n = int(input())
print(2*(n+1) - 1)
solve(n,1,2,3)