N = int(input())
arr = list(map(int, input().split()))
arr.sort()
tmp,res = 0, 0
for i in arr:
    res += tmp+i
    tmp += i
print(res)