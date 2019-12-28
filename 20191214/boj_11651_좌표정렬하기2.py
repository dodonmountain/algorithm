L = int(input())
arr = []
for i in range(L):
    x, y = map(int, input().split())
    arr.append((x,y))
arr.sort(key=lambda x:(x[1],x[0]))
for i in range(L):
    print(*arr[i])