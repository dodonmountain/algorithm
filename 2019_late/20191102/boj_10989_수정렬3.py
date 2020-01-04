import sys

arr = [0] * 10005

n = int(sys.stdin.readline())

for i in range(n):
    arr[int(sys.stdin.readline())] += 1

for i in range(n):
    for j in range(arr[i]):
        print(i)