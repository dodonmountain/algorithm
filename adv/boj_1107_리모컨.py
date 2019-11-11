N = int(input())
m = int(input())
available = set(range(10))
broken = set(map(int, input().split()))
available = available - broken
print(available)
ch = 100

