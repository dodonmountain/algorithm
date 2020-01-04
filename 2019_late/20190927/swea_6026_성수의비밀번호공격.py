import sys; sys.stdin = open('6026.txt')
from math import factorial
for t_case in range(int(input())):
    M, N = map(int, input().split())
    # all 
    init = M ** N
    # S(n ,k) * k! == answer

    tmp = ((M**N) - M) // 2 ** factorial(M)
    print('#{} {}'.format(t_case+1, tmp))