a, b = map(int, input().split())
delta = int(input())

time = a * 60 + b + delta

print(time // 60 % 24, time % 60)