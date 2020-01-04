from collections import deque
n, k = map(int, input().split())
arr = deque(map(int, input().split()))
q = deque()
q.append(arr.popleft())
while arr:
    if arr[0] == q[0]:
        arr.popleft() 
    else:
        q.appendleft(arr.popleft())
        if len(q) > k:
            q.pop()
print(len(q))
print(*q)
