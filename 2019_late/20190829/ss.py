from collections import deque

a = deque()
for i in range(1,6):
    a.append(i)
print(a)
a.rotate(-1)
print(a)
a.rotate(1)
print(a)