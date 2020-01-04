import sys;sys.stdin=open('2580.txt')
from pprint import pprint


board = [list(map(int, input().split())) for _ in range(9)]
pprint(board)