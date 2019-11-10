from collections import deque
N = int(input())

cards = deque(range(1, N+1))
while True:
    a = cards.popleft()
    if not cards:
        break
    cards.append(cards.popleft())
print(a)