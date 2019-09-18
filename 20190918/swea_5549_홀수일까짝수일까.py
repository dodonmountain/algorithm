import sys
sys.stdin = open('5549.txt')

T = int(input())

for t_case in range(T):
    n = int(input())
    if n & 1:
        print('#{} {}'.format(t_case+1,'Odd'))
    else:
        print('#{} {}'.format(t_case+1,'Even'))