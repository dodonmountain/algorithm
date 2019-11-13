import sys;sys.stdin = open('brick.txt')
from pprint import pprint




T = int(input())
T = 1
for tc in range(T):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    pprint(board, width=W*10)
    