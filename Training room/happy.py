import sys
sys.stdin = open('input.txt')

T= int(input())
for t_case in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    arr.pop()
    arr.pop(0)
    print('#{} {}'.format(t_case+1, round(sum(arr)/len(arr))))

            