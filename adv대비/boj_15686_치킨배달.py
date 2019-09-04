import sys
sys.stdin = open('15686.txt')
from pprint import pprint

from collections import deque
from itertools import combinations as cb

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]
def solve(s):
    tmp = []
    for k in goal:
        tmp.append(abs(s[0] - k[0]) + abs(s[1] -k[1]))
    return min(tmp)

N, M = map(int, input().split())
city = []
for _ in range(N):
    city.append(list(map(int, input().split())))
chicken, houses, answer = [],[],[]
# 치킨집 찾기
for qq in range(N):
    for ww in range(N):
        if city[qq][ww] == 2:
            chicken.append((qq,ww))
        if city[qq][ww] == 1:
            houses.append((qq,ww))
for chance in list(cb(chicken,M)):
    result = 0
    goal = []
    for _ in range(M):
        goal.append(chance[_])
    for home in houses:
        result += solve(home)
    answer.append(result)
print(min(answer))




    
