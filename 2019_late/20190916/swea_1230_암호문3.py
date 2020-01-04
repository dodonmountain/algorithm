import sys
sys.stdin = open('1230.txt')

T = 10
for t_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    Task = int(input())
    task = list(input().split())
    i = 0
    while i < len(task):
        if task[i] == 'I':
            x,y = int(task[i+1]), int(task[i+2])
            for k in range(y-1, -1, -1):
                arr.insert(x, int(task[i+3+k]))
            i += 3 + y
        elif task[i] =='D':
            x,y = int(task[i+1]), int(task[i+2])
            for k in range(y):
                arr.pop(x)
            i += 3
        elif task[i] == 'A':
            y = int(task[i+1])
            for k in range(y):
                arr.append(int(task[i+2+k]))
            i += 2 + y
    res = []
    for i in range(10):
        res.append(arr[i])
    print('#{}'.format(t_case+1), *res)
