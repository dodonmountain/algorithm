import sys; sys.stdin = open('1859.txt')

for t_case in range(int(input())):
    N = int(input()); res = 0
    arr = list(map(int, input().split()))
    for i in range(N-1, -1, -1):
        tmp = 0
        for j in range(i -1, -1, -1):
            if tmp < arr[j] - arr[i]:
                tmp = arr[j] - arr[i]
        res += tmp
    print('#{} {}'.format(t_case+1, res))