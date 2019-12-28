import sys
input = sys.stdin.readline

L = int(input())
arr = []
for i in range(L):
    x, y = input().split()
    x = int(x)
    arr.append((x,y,i))
arr.sort(key=lambda x:(x[0],x[2]))
for i in range(L):
    print(f'{arr[i][0]} {arr[i][1]}')