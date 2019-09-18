import sys
sys.stdin = open('3499.txt')

T = int(input())

for t_case in range(T):
    N = int(input())
    right = list(input().split())
    left = []
    if N & 1:
        mid = N//2 + 1
    else:
        mid = N//2
    for i in range(mid):
        left.append(right.pop(0))
    res = []
    while right:
        res.append(left.pop(0))
        res.append(right.pop(0))
    if left:
        res.append(left.pop(0))
    print('#{}'.format(t_case+1), *res)