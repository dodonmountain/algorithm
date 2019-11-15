N = int(input())
arr = []
while N:
    arr.append(N % 10)
    N //= 10
arr.sort(reverse=True)
for i in arr:
    print(i, end='')