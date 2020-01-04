def digit(n):
    lst = []
    while n:
        lst.append(n%10)
        n //= 10
    return lst[::-1]

N = int(input())
M = int(input())
if M:
    broken = set([map(int, input().split())])
ch = 100
target = digit(N)
for i in range(10):
    if i not in broken:
        if target[0] <= i:
            minnow = i
            break
for i in range(9,-1,-1):
    if i not in broken:
        if target[0] >= i:
            maxnow = i
            break
print(minnow, maxnow)