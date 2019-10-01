import sys;sys.stdin = open('4050.txt')

for t_case in range(int(input())):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    stack = []
    price = 0
    while arr:
        if len(stack) == 3:
            price += stack[0] + stack[1]
            stack = []
        stack.append(arr.pop())
    if stack:
        if len(stack) == 3:
            price += stack[0] + stack[1]
        else:
            price += sum(stack)
    print('#{} {}'.format(t_case+1, price))
