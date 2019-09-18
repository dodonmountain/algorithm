import sys
sys.stdin = open('5431.txt')

T = int(input())

for t_case in range(T):
    N, K = map(int, input().split())
    arr = set(map(int, input().split()))
    students = set(range(1,N+1))
    res = sorted(list(students - arr))
    print('#{}'.format(t_case+1), *res)
    