arr = list(input())
N = len(arr)
stack = []
count_stick = 0
fragment = 0
for i in range(N):
    if arr[i] == '(':
        stack.append(arr[i])
        count_stick += 1
        flag = True
    elif arr[i] == ')' and flag:
        count_stick -= 1
        fragment += count_stick
        flag = False
    else:
        stack.append(arr[i])
        count_stick -= 1
        fragment += 1
        flag = False
print(fragment)