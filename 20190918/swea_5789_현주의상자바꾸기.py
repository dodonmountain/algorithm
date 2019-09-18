import sys
sys.stdin = open('5789.txt')

T = int(input())

for t_case in range(T):
    N, Q = map(int, input().split())
    box = [0 for _ in range(1, N + 1)]
    for i in range(1, Q+1):
        L ,R = map(int, input().split())
        L -= 1; R -= 1
        for k in range(L, R+1):
            box[k] = i
    print('#{}'.format(t_case+1), *box)

