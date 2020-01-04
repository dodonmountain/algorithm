import sys
sys.stdin = open('5189.txt')

T = int(input())

def perm(s):
    if len(s) == (N-1):
        cand.append([1,*s,1])
        return
    for i in range(2, N+1):
        if not used[i]:
            used[i] = 1
            s.append(i)
            perm(s)
            s.pop()
            used[i] = 0

for t_case in range(T):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    used = [0] * (N+1)
    cand = []
    perm([])
    res = 10000
    for case in cand:
        tmp = 0
        for i in range(len(case)-1):
            tmp += board[case[i]-1][case[i+1]-1]
        if tmp < res:
            res = tmp
    print('#{} {}'.format(t_case+1, res))