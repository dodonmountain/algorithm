import sys
sys.stdin = open('6692.txt')

T = int(input())

for t_case in range(T):
    N = int(input())
    res = 0.000000
    for i in range(N):
        a, b = input().split()
        a, b = float(a), int(b)
        res += a*b
    print('#{} {}'.format(t_case+1, res))
        