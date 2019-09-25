import sys; sys.stdin = open('5432.txt')

for t_case in range(int(input())):
    arr = list(input())
    N = len(arr)
    stack = []
    count_stick = 0
    fragment = 0
    for i in range(N):
        # print('인덱스', i)
        # print('조각의갯수: ',fragment)
        # stick start
        if arr[i] == '(':
            stack.append(arr[i])
            count_stick += 1
            flag = True
        # razr
        elif arr[i] == ')' and flag:
            count_stick -= 1
            fragment += count_stick
            flag = False
        else:
            stack.append(arr[i])
            count_stick -= 1
            fragment += 1
            flag = False
    print('#{} {}'.format(t_case+1, fragment))