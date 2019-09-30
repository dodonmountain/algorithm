import sys; sys.stdin = open('5207.txt')

def bin_search(goal, l, r, direc):
    global cnt
    m = (l + r) >> 1
    if arr_A[m] == goal:
        cnt += 1
        return
    elif goal > arr_A[m]:
        if direc == 'left':
            bin_search(goal, m + 1, r, 'right')
        return 
    elif goal < arr_A[m]:
        if direc == 'right':
            bin_search(goal, l, m - 1, 'left')
        return 

for t_case in range(int(input())):
    N, M = map(int, input().split())
    arr_A = sorted(list(map(int, input().split())))
    arr_B = sorted(list(map(int, input().split())))
    tmp_mid = N-1 >> 1
    cnt = 0
    for i in arr_B:
        if i > arr_A[tmp_mid]:
            direc = 'left'
        else:
            direc = 'right'
        bin_search(i, 0, N-1, direc)
    print('#{} {}'.format(t_case+1, cnt))
    