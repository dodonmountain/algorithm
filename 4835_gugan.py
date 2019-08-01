T = int(input())
def my_sum(num):
    result = 0
    for i in range(len(num)):
        result += num[i]
    return result
for t_case in range(1,T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    tmpmx = 0
    tmpmin = 999999999999999999999
    tmplst = []
    for j in range(N-M+1):
        tmplst = []
        for i in range(M):
            tmplst.append(lst[i+j])
        if my_sum(tmplst) > tmpmx:
            tmpmx = my_sum(tmplst)
    for j in range(N-M+1):
        tmplst = []
        for i in range(M):
            tmplst.append(lst[i+j])
        if my_sum(tmplst) < tmpmin:
            tmpmin = my_sum(tmplst)
    print('#{} {}'.format(t_case, (tmpmx-tmpmin)))