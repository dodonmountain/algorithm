import sys;sys.stdin = open('input2.txt')

T = int(input())

for tc in range(T):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    