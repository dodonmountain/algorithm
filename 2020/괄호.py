import sys;sys.stdin=open('9012.txt')
def check(arr):
    stack = []
    for p in arr:
        if p == '(':
            stack.append(p)
        else:
            if stack:
                stack.pop()
            else:
                return False
    return not bool(stack)

for tc in range(int(input())):
    arr = list(input())
    print('YES' if check(arr) else 'NO')
