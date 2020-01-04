# https://www.acmicpc.net/problem/2231
import sys
sys.stdin = open("input.txt")
N = int(input())

def bh(num):
    original = num
    tmp = []
    if num < 10:
        return -1
    else:
        while num:     
            tmp.append(num % 10)
            num = num // 10
        return num + sum(tmp) + original

for i in range(N + 1):
    if i == N:
        print(0)
    elif bh(i) == N:
        print(i)
        break