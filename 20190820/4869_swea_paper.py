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









'''
    # 주어진 최대 넓이 20을 N으로 나눈수가 넓이가 20인 종이를 사용 할 수 있는 최대치
    for i in range(int(N / 20)): # range(1.5 - > 1)
        widthChoice = 2**(i+1) #2, 4, 8, 16, 32, 64, 128, 256,...
        totalBar = int(N/10 - (i+1)) # 3 - 1 = 2 
        width20bar = i+1 # 1 
        width10bar = int(N/10 - 2*(i+1)) # 3 - 2 = 1
        lineUp = math.factorial(totalBar)/(math.factorial(width20bar)*math.factorial(width10bar)) # 2! / 1! * 1!
        res += int(widthChoice*lineUp) # 경우의 수 * 쌓인 방향 = 2 * 2 = 4

    res += 1
    print('#{} {}'.format(t_case + 1, res))
'''