import sys
sys.stdin = open("inputb.txt")

N, M, V = map(int, input().split())
lines = []
for i in range(M):
    lines += list(map(int,input().split()))

lines.extend(lines[::-1])
print(lines)
