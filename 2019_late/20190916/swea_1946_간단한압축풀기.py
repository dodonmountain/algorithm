import sys
sys.stdin = open('1946.txt')

T = int(input())

for t_case in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        c, k = input().split(); k = int(k)
        arr.extend(list(c*k))
    print('#{}'.format(t_case+1))
    for i in range(len(arr)//10 + 1):
        tmp = ''
        for k in range(10):
            if arr:
                tmp += arr.pop(0)
            else:
                break
        print(tmp)
        