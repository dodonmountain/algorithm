import sys
sys.stdin = open("17144.txt")
from pprint import pprint
r,c,t = map(int,input().split())
board = []
for i in range(r):
    board.append(list(map(int, input().split())))
for i in range(r):
    for j in range(r):
        