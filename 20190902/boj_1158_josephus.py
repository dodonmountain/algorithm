from collections import deque
n, t = map(int, input().split())
line = deque(range(1, n + 1))
joseph, res = [], []
while line:
    line.rotate(-(t-1))
    res.append(line.popleft())
print("<{}>".format(', '.join(map(str, res))))
