S = input()
counter = [-1] * 26
for i in S:
    counter[ord(i)-97] = S.index(i)
for j in counter:
    print(j, end=' ')
