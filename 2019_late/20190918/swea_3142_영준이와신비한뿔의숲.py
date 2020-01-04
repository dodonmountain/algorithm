import sys
sys.stdin = open('3142.txt')

T = int(input())

for t_case in range(T):
    n, m = map(int, input().split())
    arr = [1] * m
    i = 0
    while True:
        if sum(arr) == n:
            break
        else:
            arr[i] = 2
            i += 1
    print('#{}'.format(t_case+1),arr.count(1),arr.count(2))
        