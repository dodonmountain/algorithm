import sys
sys.stdin = open("14501.txt")

from collections import deque
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
visit = [0] * (N+1)
MAX = -1
back(0,0,[])
print(MAX)
