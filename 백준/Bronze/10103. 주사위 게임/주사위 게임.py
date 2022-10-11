T = int(input())
score_a = 100
score_b = 100

for _ in range(T):
    a, b = map(int, input().split())
    if a > b:
        score_b -= a
    elif a < b:
        score_a -= b

print(score_a)
print(score_b)