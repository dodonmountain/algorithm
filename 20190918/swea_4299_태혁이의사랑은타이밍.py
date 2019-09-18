import sys
sys.stdin = open('4299.txt')

T = int(input())

for t_case in range(T):
    d,h,m = map(int, input().split())
    start = 16511
    end = d * 24 * 60 + h * 60 + m 
    if end - start < 0:
        print('#{} {}'.format(t_case+1, -1))
    else:
        print('#{} {}'.format(t_case+1, end-start))