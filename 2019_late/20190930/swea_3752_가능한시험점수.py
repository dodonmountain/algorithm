import sys; sys.stdin = open('3752.txt')

for t_case in range(int(input())):
    N = int(input())
    q = sorted(map(int, input().split()))
    _max = sum(q)
    visit = [False] * 10000; visit[0] = True
    while q:
        now = q.pop()
        for i in range(_max-1, -1, -1):
            if visit[i]:visit[i + now] = True
    print('#{} {}'.format(t_case+1, sum(visit)))