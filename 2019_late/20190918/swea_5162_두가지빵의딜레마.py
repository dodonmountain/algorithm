import sys
sys.stdin = open('5162.txt')

T = int(input())

for t_case in range(T):
    a, b, money = map(int, input().split())
    if a < b:
        print('#{} {}'.format(t_case+1, money // a))
    else:
        print('#{} {}'.format(t_case+1, money // b))