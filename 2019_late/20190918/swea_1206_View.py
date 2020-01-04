import sys
sys.stdin = open('1206.txt')

for t_case in range(10):
    N = int(input())
    arr = list(map(int, input().split()))
    res = 0
    for i in range(2, N-2):
        comp = [arr[i-2], arr[i-1], arr[i+1], arr[i+2]]
        if arr[i] > max(comp):
            res += arr[i] - max(comp)
    print('#{} {}'.format(t_case+1, res))
        