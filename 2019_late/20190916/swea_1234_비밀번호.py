import sys
sys.stdin = open('1234.txt')

for t_case in range(10):
    N, arr = map(int, input().split())
    arr = list(map(int, list(str(arr))))
    flag = True
    while flag:
        cnt = 0
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                arr.pop(i)
                arr.pop(i)
                break
            else:
                cnt += 1
        if cnt == len(arr) - 1:
            flag = False
    print('#{} {}'.format(t_case+1, int(''.join(map(str, arr)))))
        