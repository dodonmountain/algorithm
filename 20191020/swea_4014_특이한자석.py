import sys;sys.stdin = open('4014.txt')

from collections import deque

def solve(t, com):
    rotate = [False] * 4
    if t == 1:
        rotate[0] = com
        if mag[0][2] != mag[1][-2]:
            rotate[1] = -com
            if mag[1][2] != mag[2][-2]:
                rotate[2] = com
                if mag[2][2] != mag[3][-2]:
                    rotate[3] = -com
    elif t == 2:
        rotate[1] = com
        if mag[1][2] != mag[2][-2]:
            rotate[2] = -com
            if mag[2][2] != mag[3][-2]:
                rotate[3] = com
        if mag[1][-2] != mag[0][2]:
            rotate[0] = -com
    elif t == 3:
        rotate[2] = com
        if mag[2][2] != mag[3][-2]:
            rotate[3] = -com
        if mag[2][-2] != mag[1][2]:
            rotate[1] = -com
            if mag[1][-2] != mag[0][2]:
                rotate[0] = com
    else:
        rotate[3] = com
        if mag[2][2] != mag[3][-2]:
            rotate[2] = -com
            if mag[1][2] != mag[2][-2]:
                rotate[1] = com
                if mag[0][2] != mag[1][-2]:
                    rotate[0] = -com
    for i in range(4):
        if rotate[i] != False:
            mag[i].rotate(rotate[i])

T = int(input())

for tc in range(T):
    K = int(input())
    mag = [deque(map(int, input().split())) for _ in range(4)]
    for i in range(K):
        target, com = map(int, input().split())
        solve(target, com)
    ans = 0; k = 1
    for i in range(4):
        ans += mag[i][0] * k
        k *= 2
    print('#{} {}'.format(tc+1, ans))