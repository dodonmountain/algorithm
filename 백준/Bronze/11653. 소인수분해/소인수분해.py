n = int(input())
answer = []
i = 2
while n > 1:
    if not (n % i):
        answer.append(i)
        n //= i
        i = 2
    else:
        i += 1
for a in sorted(answer):
    print(a)
