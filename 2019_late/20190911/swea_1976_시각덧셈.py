import sys
sys.stdin = open('1976.txt')

T = int(input())

for t_case in range(T):
    arr = list(map(int, input().split()))
    a = arr[0]*60 + arr[1] 
    b = arr[2]*60 + arr[3]
    res = divmod(a+b, 60)
    time = res[0]
    if res[0] > 12:
        time = res[0] - 12
    print('#{} {} {}'.format(t_case+1,time,res[1]))