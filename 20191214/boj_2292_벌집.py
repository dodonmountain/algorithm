import sys
input = sys.stdin.readline

N = int(input())
if N == 1:
    print(1)
else:
    memo = [2]
    for i in range(1, 28000):
        k = memo[i-1] + (6 * i)
        if k > N:
            print(i + 1)
            break
        memo.append(k)