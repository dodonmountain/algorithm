s=int(input())
count = 0
now = 0

for n in range(1,s+1):
    count += 1
    if (now + n) > s:
        break
    now += n
if (s == 1):
    print(1)
else: 
    print(count - 1)