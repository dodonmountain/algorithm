import sys
sys.stdin = open('3233.txt')

T = int(input())

for t_case in range(T):
    a, b = map(int, input().split())
    if a == b:
        res = 1
    else:
        res = ((a // b))**2
    print('#{} {}'.format(t_case+1, res))
