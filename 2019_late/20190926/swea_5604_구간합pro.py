import sys; sys.stdin = open('5604.txt')


def solve(num):
    tmp = 0
    if num < 10:
        return num
    while num:
        tmp += num % 10
        num //= 10
    return tmp
arr = [0]
for i in range(1, 101):
    arr.append(solve(i)+arr[i-1])
for i in range(2,90,10):
    print(arr[i])

for t_case in range(int(input())):
    a, b = map(int, input().split())

    if a == 0:
        a = 1
    res = arr[b] - arr[a-1]
    print('#{} {}'.format(t_case+1,res))