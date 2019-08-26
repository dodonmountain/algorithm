import sys
sys.stdin = open("input4881.txt")
from itertools import permutations, chain

T = int(input())

for t_case in range(T):
    N = int(input())
    tmp, arr, arr2, res = [], [], [], [0]*N
    for numbers in range(N):
        arr.append(list(map(int, input().split())))
    for i in range(N):
        for j in range(N):
            tmp.append(arr[j][i])
        arr2.append(tmp)
        tmp = []
    stack = []
    chain.from_iterable(arr2)
    print(arr2)