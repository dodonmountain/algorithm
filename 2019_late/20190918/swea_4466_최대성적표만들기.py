import sys
sys.stdin = open('4466.txt')

T = int(input())

for t_case in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    res = 0
    for i in range(K):
        res += arr[i]
    print('#{} {}'.format(t_case+1, res))