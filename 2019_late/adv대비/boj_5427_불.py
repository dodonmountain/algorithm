import sys
sys.stdin = open('5427.txt')
from pprint import pprint

T = int(input())
for t_case in range(T):
    w, h = map(int, input().split())
    building = []
    for _ in range(h):
        building.append(list(input()))
    pprint(building,width=w*10)
