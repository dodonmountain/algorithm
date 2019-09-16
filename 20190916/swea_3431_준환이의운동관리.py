import sys
sys.stdin = open('3431.txt')

T = int(input())

for t_case in range(T):
    l, u, x = map(int, input().split())
    if x > u:
        print('#{} {}'.format(t_case+1, -1))
    elif x >= l:
        print('#{} {}'.format(t_case+1, 0))
    else:
        print('#{} {}'.format(t_case+1, l-x))
