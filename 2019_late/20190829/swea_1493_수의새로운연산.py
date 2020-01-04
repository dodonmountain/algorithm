import sys
sys.stdin = open('1493.txt')

T = int(input())
def king(n, k):
    if n < 2:
        return 1
    else:
        return king(n-1,k) + n + k
board = []
print(king(2,3))
