import sys
sys.stdin = open('13458.txt')
N = int(input())
if N == 1:
    A = [int(input())]
else:
    A = list(map(int, input().split()))
B, C = map(int, input().split())
res = 0
bugam = 0
for i in range(N):
    if A[i] <= B:
        res += 1
    else:
        res += 1
        A[i] -= B
        bugam += A[i]//C
        if A[i]%C:
            bugam += 1
res += bugam
print(res)