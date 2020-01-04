import sys; sys.stdin = open('5622.txt')

dial = list(input())
arr = []
for i in dial:
    arr.append(((ord(i) - 65) // 3 + 2))
print(sum(arr)+len(arr))