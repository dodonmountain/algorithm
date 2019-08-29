import sys
sys.stdin = open('2597.txt')
N = int(input())
color = []
newblue, newyellow = [], []
for _ in range(3):
    color.append(list(map(int, input().split())))

ja = {x: '없' for x in range(1,N+1) }
for i in color[0]:
    ja[i] = '빨'
for i in color[1]:
    ja[i] = '파'
for i in color[2]:
    ja[i] = '노'
jaja = list(ja.values())
print(jaja)
if len(jaja) % 2:
    left = jaja[:(color[0][0]+color[0][1])//2]
    right = jaja[(color[0][0]+color[0][1])//2:]
else:
    left = jaja[:(color[0][0]+color[0][1])//2 + 1]
    right = jaja[(color[0][0]+color[0][1])//2 + 1:]
if len(left) > len(right):
    right = right[::-1]
    for i in range(len(right)):
        if left[i] =='없' and right[i] != '없':
            left[i] = right[i]
    jaja = left
else:
    left = left[::-1]
    for i in range(len(left)):
        if right[i] == '없' and left[i] != '없':
            right[i] = left[i]
    jaja = right
print(jaja)
for s in range(len(jaja)):
    if jaja[s] == '파':
        newblue.append(s)
if jaja.count('파') > 1:
    if len(jaja) % 2:
        left = jaja[:(newblue[0] + newblue[1]) // 2]
        right = jaja[(newblue[0] + newblue[1]) // 2:]
    else:
        left = jaja[:(newblue[0] + newblue[1]) // 2 + 1]
        right = jaja[(newblue[0] + newblue[1]) // 2 + 1:]
    if len(left) > len(right):
        right = right[::-1]
        for i in range(len(right)):
            if left[i] == '없' and right[i] != '없':
                left[i] = right[i]
        jaja = left
    else:
        left = left[::-1]
        for i in range(len(left)):
            if right[i] == '없' and left[i] != '없':
                right[i] = left[i]
        jaja = right
print(jaja)
for s in range(len(jaja)):
    if jaja[s] == '노':
        newyellow.append(s)
if jaja.count('노') > 1:
    if len(jaja)%2:
        left = jaja[:(newyellow[0] + newyellow[1]) // 2]
        right = jaja[(newyellow[0] + newyellow[1]) // 2:]
    else:
        left = jaja[:(newyellow[0] + newyellow[1]) // 2 + 1]
        right = jaja[(newyellow[0] + newyellow[1]) // 2 + 1:]
    if len(left) > len(right):
        right = right[::-1]
        for i in range(len(right)):
            if left[i] == '없' and right[i] != '없':
                left[i] = right[i]
        jaja = left
    else:
        left = left[::-1]
        for i in range(len(left)):
            if right[i] == '없' and left[i] != '없':
                right[i] = left[i]
        jaja = right
print('노랑이후')
print(jaja)
print('{:.1f}'.format(len(jaja)))
