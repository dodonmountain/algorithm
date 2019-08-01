A, B, C = map(int, input().split())
n = A//(C-B) if C > B else -1
while True:
    if A+(B*n) < C*n:
        break
    elif n == -1:
        break
    else:
        n += 1
print(n)