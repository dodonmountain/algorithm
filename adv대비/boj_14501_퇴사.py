import sys
sys.stdin = open("14501.txt")

from collections import deque
N = int(input())
arr = [(0, 0)] + [tuple(map(int,input().split())) for _ in range(N)]

ans = 0
def backtrack(day, p): # day: 결정할 날짜, p: 지금까지의 이익

    if day > N + 1: return
    if day == N + 1:
        global ans
        ans = max(ans, p)
        return

    # 상담을 하는 경우
    backtrack(day + arr[day][0], p + arr[day][1])
    # 상담을 하지않는 경우
    backtrack(day+1, p)
backtrack(1,0)
print(ans)