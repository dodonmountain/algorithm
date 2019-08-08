import pprint

a = [[0]*101 for _ in range(101)]

lst = [0, 0, 10, 10]

for j in range(lst[3]):
    for i in range(lst[2]):
        a[100-lst[0]-j][lst[1] + i] = '1'

lst = [2, 2, 6, 6]

for j in range(lst[3]):
    for i in range(lst[2]):
        a[100-lst[0]][lst[1] + i] = '2'
case = 1
result = 0

for i in range(101):
    for j in range(101):
        if a[i][j] == str(case):
            result += 1

print(''.join(map(str, a)))

