import sys;sys.stdin = open('stemcell.txt')

T = int(input())

for tc in range(1, T):
    N, M, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    while K:
        