import sys
sys.stdin = open("input.txt")

T = int(input())

for t_case in range(T):
    N = int(input())
    # not N % 10
    # cover up 20*N
    # with 2 elem, 20 x 10 + 20 x 20
    only small = 20 x 10 x N
    