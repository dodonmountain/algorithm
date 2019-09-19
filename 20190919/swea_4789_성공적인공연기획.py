import sys
sys.stdin = open('4789.txt')

T = int(input())

for t_case in range(T):
    arr = list(map(int, list(input())))
    need,now = 0,0
    for i in range(len(arr)):
        if now < i:
            if arr[i]:
                need += i - now
                now += i - now
        now += arr[i]
    print('#{} {}'.format(t_case+1, need))