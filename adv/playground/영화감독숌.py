n = int(input())
cnt = 0
for i in range(666, 3000000):
    flag = False
    temp = i
    while temp:
        if temp % 1000 == 666:
            flag = True
            break
        temp //= 10
    if flag:
        cnt += 1
        if cnt == n:
            print(i)
            break

