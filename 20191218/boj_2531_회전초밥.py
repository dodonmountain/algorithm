import sys;sys.stdin = open('2531.txt')

from collections import deque
N, d, k, c = map(int, input().split())
q = deque([int(input()) for _ in range(N)])
print(q)