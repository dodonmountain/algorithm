n = int(input())
arr = set()
for i in range(n):
    arr.add(input())
arr = sorted(list(arr))
arr.sort(key= lambda x:(len(x)))
for i in arr:
    print(i)