stack = []
n = int(input())
cmd = [input() for _ in range(n)]
for m in cmd:
    if m == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    elif m == 'size':
        print(len(stack))
    elif m == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif m =='pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        a, b = m.split()
        stack.append(int(b))
