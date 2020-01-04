import sys
sys.stdin = open('input4881.txt', 'r')

def backtracking(k, n, sum_temp):
    global min_sum
    if k == n:
        # print('sum_temp_final: {}'.format(sum_temp))
        if min_sum > sum_temp:
            min_sum = sum_temp
        return
    if sum_temp > min_sum: # 시간 초과 나서 가지치기 해줌!
        return
    for i in range(N):
        if used_col[i]:
            continue
        sum_temp += lst[k][i]
        # print('lst[{}][{}]: {}, sum_temp: {}'.format(k, i, lst[k][i], sum_temp))
        used_col[i] = True
        backtracking(k + 1, n, sum_temp)
        sum_temp -= lst[k][i]
        used_col[i] = False

for t in range(1, int(input()) + 1):
    N = int(input())
    lst = []
    for j in range(N):
        lst.append(list(map(int, input().split())))
    used_col = [False] * N
    min_sum = 10*N
    backtracking(0, N, 0)
    print('#{} {}'.format(t, min_sum))