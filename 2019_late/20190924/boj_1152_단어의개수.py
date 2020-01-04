word = input()
cnt = 0
if word[0] == ' ':
    cnt -= 1
if word[-1] == ' ':
    cnt -= 1
cnt += word.count(' ')
print(cnt+1)
