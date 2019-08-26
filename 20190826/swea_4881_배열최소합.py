import sys
sys.stdin = open("input4881.txt")
from collections import deque
from copy import deepcopy
print(10**10)
# T = int(input())

# for t_case in range(T):
#     N = int(input())
#     tmp, arr, arr2, res, stack = [], [], deque(), [0]*N, []
#     for numbers in range(N):
#         arr.append(list(map(int, input().split())))
#     for i in range(N):
#         for j in range(N):
#             tmp.append(arr[j][i])
#         arr2.append(tmp)
#         tmp = []
#     print(arr2)
#     # print("#{} {}".format(t_case+1, min(res)))