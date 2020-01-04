import sys
sys.stdin = open("input1224.txt")

T = 1

for t_case in range(T):
    l = int(input())
    ipt = list(input())
    stack = []
    for i in ipt:
        if i == '.':
            if len(stack) > 1:
                res = 'error'
            else:
                res = stack.pop()
                break
        elif i not in '+-*/()':
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
            elif i == '(':
                pass
            elif i == ')':
                pass
            else:
                res = 'error'
                break
    print(ipt)
    # print('#{} {}'.format(t_case+1, res))