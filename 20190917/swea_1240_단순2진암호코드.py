import sys
sys.stdin = open('1240.txt')

T = int(input())
T = 1
for t_case in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    arr = list(map(int, arr))
    for y in range(N):
        for x in range(M):
            if arr[y][x] == 1:
                break
    for i in range(0, 56, 7):
        print(arr[y][x + i:x+i+7])