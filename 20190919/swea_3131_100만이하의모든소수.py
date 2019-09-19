arr = [2]
for i in range(3, 1000000, 2):
    flag = True
    for j in range(2, int(i ** 0.5)+1):
        if not i % j:
            flag = False
            break
    if flag:
        arr.append(i)
print(*arr)