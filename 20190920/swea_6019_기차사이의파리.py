import sys
sys.stdin = open('6019.txt')

T = int(input())

for t_case in range(T):
    d,a,b,f = map(int, input().split())
    road = [0] * d
    c = a + b
    t = 1
    print('#{} {:.10f}'.format(t_case+1, d/c*f))
