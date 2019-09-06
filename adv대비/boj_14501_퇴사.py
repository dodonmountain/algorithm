import sys
sys.stdin = open("14501.txt")

def back(N, arr, arr2):
    for i in range(0, N - 1):
        left = N
        for j in range(0, N):

        print(arr[i])
N = int(input())
arr,arr2 = [], []
for _ in range(N):
    a,b = input().strip().split()
    arr.append(int(a))
    arr2.append(int(b))
visit = [0] * (N+1)
back(N,arr,arr2)
