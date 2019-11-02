from pprint import pprint
import sys
sys.stdin = open('1085.txt')


x, y, w, h = map(int, input().split())
board = [[0] * (w+1) for _ in range(h+1)]
board[h-y][x] = 1
print(min(
    [
        (h - (h-y)),
        (h-y),
        (w-x),
        (x)
    ]
))
