import sys
sys.stdin = open('input.txt')
N = int(input())
numbers = list(map(int, input().split()))
result = len(numbers)
for i in range(N):
    if numbers[i] == 1:
        result -= 1
    for k in range(2, numbers[i]):
        if numbers[i] % k == 0:
            result -= 1
            break
print(result)