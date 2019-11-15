import sys
sys.stdin = open('high.txt')

L = int(input())
cost = list(map(int, input().split()))
N = int(input())
trucks = []
for i in range(N):
    A, B, C = map(int, input().split())
    trucks.append((A,B,C))
K = int(input())
