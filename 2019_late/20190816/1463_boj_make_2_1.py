
num = int(input())

def divide(num):
    cnt = 0
    while num > 1:
        if not num % 3:
            num /= 3
            cnt += 1
        elif not num % 2:
            num /= 2
            cnt += 1
        else:
            num -= 1
            cnt += 1
    return cnt
i = 0
tmp = divide(num)
while num:
    print(tmp)
    num = num - 1
    tmp2 = divide(num)
    if tmp > tmp2:
        tmp = tmp2

print(tmp - 1)





