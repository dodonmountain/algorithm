import sys
sys.stdin = open('3809.txt')

T = int(input())

for t_case in range(T):
    N = int(input())
    if N > 1:
        arr = []
        while len(arr) < N:
            arr.extend(list(map(str, input().split())))
        word = ''.join(arr)
        for i in range(2000):
            if str(i) not in word:
                print('#{} {}'.format(t_case+1, i))
                break
    else:
        arr = int(input())
        for i in range(10):
            if i != arr:
                break
        print('#{} {}'.format(t_case+1, i))