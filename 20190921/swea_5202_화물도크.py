import sys
sys.stdin = open('5202.txt')

def check(arr):
    for i in range(arr[2]):
        if scheduled[arr[0] + i]:
            return False
    return True

for t_case in range(int(input())):
    N = int(input())
    arr, cnt, scheduled = [], 0, [0] * 24
    for i in range(N):
        a, b = map(int, input().split())
        arr.append([a,b,b-a])
    arr.sort(key=lambda arr: (arr[2], arr[0]))
    for i in range(N):
        if check(arr[i]):
            cnt += 1
            for j in range(arr[i][2]):
                scheduled[arr[i][0] + j] = 1
    print('#{} {}'.format(t_case+1, cnt))