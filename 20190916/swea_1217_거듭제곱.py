import sys
sys.stdin = open('1217.txt')

T = 10
def solve(s, k):
    if k == m:
        return s
    else:
        return solve(s*n, k+1) 
for t_case in range(T):
    num = int(input())
    n, m = map(int,input().split())
    print('#{} {}'.format(num, solve(n, 1)))