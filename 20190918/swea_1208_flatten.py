import sys
sys.stdin = open('1208.txt')

for t_case in range(10):
    dump = int(input())
    arr = list(map(int, input().split()))
    for i in range(dump):
        arr[-1] -= 1
        arr[0] += 1
        arr.sort()
    print('#{} {}'.format(t_case+1, arr[-1] - arr[0]))