import sys;sys.stdin=open('10816.txt')

from collections import Counter
n = int(input())
cards = Counter(list(map(int, input().split())))
m = int(input())
arr = list(map(int, input().split()))
res = []
for num in arr:
    res.append(cards[num])
print(*res)