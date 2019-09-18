import sys
sys.stdin = open('5515.txt')

T = int(input())

for t_case in range(T):
    m, d = map(int, input().split())
    mth = [0,31,29,31,30,31,30,31,31,30,31,30,31]
    for i in range(m):
        d += mth[i]
    print('#{} {}'.format(t_case+1, (d-4)%7))