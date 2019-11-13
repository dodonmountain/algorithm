from pprint import pprint
import sys
sys.stdin = open('home.txt')

cost = [1] * 31
for i in range(1, 31):
    cost[i] = cost[i-1] + (4 * i)

def getBenefit(x, y):
    cnt = 0
    for house in houses:
        dx, dy = house
        distance = abs(x-dx) + abs(y-dy)
        if distance <= k:cnt += 1
    return cnt

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    houses = []
    total = N * N
    maxhouse = 1
    for i in range(1, 30):
        if cost[i] > total * 2:
            MaxK = i + 1
            break
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                houses.append((i, j))
    for k in range(MaxK-1,0,-1):
        for i in range(k//2, N-(k//2) + 1):
            for j in range(k//2, N-(k//2) + 1):
                tmp = getBenefit(i,j)
                if tmp * M >= cost[k]:
                    if tmp > maxhouse:
                        maxhouse = tmp
            if maxhouse == total:
                break
    print('#{} {}'.format(tc, maxhouse))
