a, b, c = map(int, input().split())
delta = int(input())

time = a * 60 * 60 + b * 60 + c + delta

print(time // 60 // 60 % 24, time // 60 % 60, time % 60)
