import sys
sys.stdin = open('2948.txt')

for t_case in range(int(input())):
    n, m = map(int, input().split())
    arr1 = set(input().split())
    arr2 = set(input().split())
    print('#{} {}'.format(t_case+1, len(arr1 & arr2)))
