import sys
sys.stdin = open("5097.txt")
from collections import deque
T = int(input())

for t_case in range(T):
    N, M = map(int, input().split())
    lst = deque(map(int,input().split()))
    lst.rotate(-M)
    print("#{} {}".format(t_case+1, lst[0]))