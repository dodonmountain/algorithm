import sys; sys.stdin = open('2386.txt')

for t_case in range(int(input())):
    N = int(input())
    arr = [int(input()) for _ in range(N)]
    lst = set()
    for say in arr:
        if say not in lst:
            lst.add(say)
        else:
            lst.remove(say)
    print('#{} {}'.format(t_case+1, len(lst)))