import sys; sys.stdin = open('2369.txt')

for t_case in range(int(input())):
    N, res = int(input()), 0
    for i in range(N):
        L, R = map(int, input().split())
        res += R - L + 1
    print(f'#{t_case+1} {res}')