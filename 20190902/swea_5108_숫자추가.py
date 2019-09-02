import sys
sys.stdin = open('5108.txt')

T = int(input())

for t_case in range(T):
    N, M, L = map(int, input().split())
    initial = list(map(int, input().split()))
    tmp = []
    for _ in range(M):
        tmp.append(list(map(int, input().split())))
    for add in tmp:
        initial.insert(add[0], add[1])
    print("#{} {}".format(t_case+1, initial[L]))