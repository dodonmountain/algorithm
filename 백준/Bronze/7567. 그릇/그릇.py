s = input()

height = 0
before = ''
for i in range(len(s)):
    if (before == s[i]):
        height += 5
    else:
        height += 10
    before = s[i]

print(height)