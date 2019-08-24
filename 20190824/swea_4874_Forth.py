import sys
sys.stdin = open("input.txt")

T = int(input())

for t_case in range(T):
    ipt = list(input().split())
    stack = []
    for i in ipt:
        if i == '.':
            if len(stack) > 1:
                res = 'error'
            else:
                res = stack.pop()
                break
        elif i not in '+-*/':
            stack.append(i)
        elif len(stack) < 2:
            res = 'error'
            break
        else:
            if i == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a+b)
            elif i == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a-b)
            elif i == '*':
                b = int(stack.pop())
                a = int(stack.pop())                
                stack.append(a*b)
            elif i == '/':
                b = int(stack.pop())
                a = int(stack.pop())                
                stack.append(a//b)
            else:
                res = 'error'
                break
    print('#{} {}'.format(t_case+1, res))