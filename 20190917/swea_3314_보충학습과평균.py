import sys
sys.stdin = open('3314.txt')

T = int(input())

for t_case in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    for i in range(5):
        if arr[i] < 40:
            arr[i] = 40
    print('#{} {}'.format(t_case+1, sum(arr)//5))