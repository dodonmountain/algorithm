import sys
sys.stdin = open("input.txt")

# 길이가 짝수면 반으로 나눌수 있지 않을까?
# 반으로 나누다 보면 언젠가 20x20의 사각형에 도달한다.
# 20x20의 경우의 수는 가로가로, 세로세로, 큰거하나의 세가지.
# 가로만을 기준으로 생각하면 가로가 20인 종이를 몇개나 고르는가의 문제이다.
# 1층만을 기준으로 나올수있는 모양은 10과 20의 두가지 모양을 나열하는것.
import pprint
import math
import itertools
T = int(input())
for t_case in range(T):
    N = int(input()) # 30
    res = 0
    for i in range(N // 20):
        floor = 2 ** (i + 1)







