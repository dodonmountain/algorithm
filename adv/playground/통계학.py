from collections import Counter
import sys
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]
dic = {}
print(round(sum(arr) / N))
arr.sort()
print(arr[(len(arr)>>1)])

if len(arr) < 3:
    print(arr[0])
else:
    ct = tuple(Counter(arr).most_common(2))
    if ct[0][1] == ct[1][1]:
        print(ct[1][0])
    else:
        print(ct[0][0])
print(max(arr) - min(arr))