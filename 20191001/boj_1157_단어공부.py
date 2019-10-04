word = input().upper()
d = dict()
for i in word:
    if i not in d.keys():
        d[i] = 1
    else:
        d[i] += 1
answer = '?'
tmp = 0
for i, n in d.items():
    if n > tmp:
        tmp = n
        answer = i
vls = list(d.values())
if vls.count(tmp) >= 2:
    print('?')
else:
    print(answer)