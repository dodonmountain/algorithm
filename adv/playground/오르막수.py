N = int(input())
cnt = 0
for i in range(10**N):
    num = i
    flag = True
    while num:
        prev = num % 10
        num //= 10
        now = num % 10
        if prev < now:
            flag = False
            break
    if flag:
        cnt += 1
print(cnt%10007)