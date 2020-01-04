import sys;sys.stdin = open('7701.txt')

for t_case in range(int(input())):
    N = int(input())
    arr = list(set([input() for _ in range(N)]))
    arr.sort(key = str)
    arr.sort(key = len)
    print('#{}'.format(t_case+1))
    for i in range(len(arr)):
        print(arr[i])