import sys
sys.stdin = open('1244.txt')

T = int(input())

for t_case in range(T):
    a, b = map(int, input().split())
    a = list(map(int, list(str(a))))
    