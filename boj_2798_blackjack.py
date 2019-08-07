import sys
input = sys.stdin.readline
import itertools

N, M = map(int, input().split())

cards = list(map(int, input().split()))
lst = list(itertools.permutations(cards,3))
tmp = -1
for i in lst:
    if sum(i) >= tmp and sum(i) <= M:
        tmp = sum(i)
    else:
        continue
print(tmp)