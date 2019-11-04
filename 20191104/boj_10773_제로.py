k = int(input())
stack = []
for i in range(k):
    num = int(input())
    if num:
        stack.append(num)
    else:
        stack.pop()
print(sum(stack))