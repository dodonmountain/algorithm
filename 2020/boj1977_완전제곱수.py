perfect_square = [0] + [i*i for i in range(1, 101)]
m = int(input())
n = int(input())
cntup = 0
for i in perfect_square:
    if m <= i <= n:
        cntup += i
if cntup:
    print(cntup)
    for i in perfect_square:
        if i >= m:
            print(i)
            break
else:
    print(-1)
