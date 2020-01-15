import sys;sys.stdin=open('boj1927.txt')

from heapq import heapify, heappop, heappush
n = int(input())
minheap = []
for _ in range(n):
    command = int(input())
    if command == 0:
        if minheap:
            print(heappop(minheap))
        else:
            print(0)
    else:
        heappush(minheap, command)