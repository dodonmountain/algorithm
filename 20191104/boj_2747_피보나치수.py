prev, pprev = 0, 1
now = 0
n = int(input())
for i in range(n):
    now = prev + pprev
    pprev = prev
    prev = now
print(now)