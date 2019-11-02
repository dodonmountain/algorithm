import sys;sys.stdin=open('input.txt')
from pprint import pprint

T = int(input())

delta = ((1, 0), (0, 1), (-1, 0), (0, -1))
T = 1
for tc in range(T):
    M, A = map(int, input().split())
    arr_a = list(map(int, input().split()))
    arr_b = list(map(int, input().split()))
    aps = [list(map(int, input().split())) for _ in range(A)]
