import sys
sys.stdin = open('ttinput.txt')
import collections, random

deque = collections.deque
T = int(input())
def s_o_matic(cards, x):
    if len(cards) % 2 == 0:
        left = cards[:len(cards)//2]
        right = cards[len(cards)//2:]
    else:
        left = cards[:len(cards)//2]
        right = cards[len(cards)//2:]
    left = deque(left)
    right = deque(right)
    tmp, tmp2, res = deque(), deque(), deque()
    if x <= len(left+right) >> 1:
        for i in range(x):
            tmp.append(right.popleft())
            tmp2.append(left.pop())
        for i in range(len(tmp)):
            res.append(tmp.popleft())
            res.append(tmp2.pop())
        return (left + res + right)
    y = N - 1 - x
    if y < len(left + right) >> 1:
        for i in range(y):
            tmp.append(left.popleft())
            tmp2.append(right.pop())
        for i in range(len(tmp)):
            res.append(tmp2.pop())
            res.append(tmp.popleft())
        return (left + res + right)

for t_case in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    cnt = 0
    king = []
    for _ in range(500):
        luck = random.randrange(1, N - 1)
        while True:
            if cnt > 4:
                break
            if cards == sorted(cards) or cards == sorted(cards,reverse=True):
                king.append(cnt)
                break
            cards = s_o_matic(cards, luck)
            cards = list(cards)
            cnt += 1
    if king:
        print(min(king))
    else:
        print(-1)





