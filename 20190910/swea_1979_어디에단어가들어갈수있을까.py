import sys
sys.stdin = open('1979.txt')
T= int(input())
T=1

for t_case in range(T):
    N, K = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    