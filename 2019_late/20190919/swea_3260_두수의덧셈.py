T = int(input())

for t_case in range(T):
    a, b = map(int, input().split())
    print('#{} {}'.format(t_case+1, a+b))