import sys
sys.stdin = open('5601.txt')

T = int(input())

for t_case in range(T):
    N = int(input())
    arr = ['1/{}'.format(N)] * N
    print('#{}'.format(t_case+1),*arr)