arr = list(map(int, list(input())))
checker = [0] * 10
for i in arr:
    checker[i] += 1
check = checker[6] + checker[9] 
if check & 1:
    check = (check//2) + 1
else:
    check = check // 2
checker[6] = check
checker[9] = 0
print(max(checker))