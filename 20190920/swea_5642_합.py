import sys
sys.stdin = open('5642.txt')


T = int(input())

for t_case in range(T):
    N = int(input())
    t = []
    arr = list(map(int, input().split()))
    for i in range(N):
        for j in range(N):
            t.append(sum(arr[i:j]))
    print('#{} {}'.format(t_case+1, max(t)))