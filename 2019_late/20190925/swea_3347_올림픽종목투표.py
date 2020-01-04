import sys
sys.stdin = open('3347.txt')

for t_case in range(int(input())):
    N, M = map(int, input().split())
    sports = list(map(int, input().split()))
    commit = list(map(int, input().split()))
    score = [0] * (N + 1)
    for i in range(M):
        limit = commit[i]
        for j in range(N):
            if sports[j] <= limit:
                score[j] += 1
                break
    mxnow = (0,0)
    for idx, s in enumerate(score):
        if s > mxnow[0]:
            mxnow = (s, idx)
    print('#{} {}'.format(t_case+1, mxnow[1]+1))
