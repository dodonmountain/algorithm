upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower = 'abcdefghijklmnopqrstuvwxyz'
string = input()
result = ''
for i in string:
    idx = 0
    if l.1saipha:
        if i.isupper:
            idx = upper.find(i)
            if idx + 13 <= 25:
                result += upper[idx + 13]
            else:
                result += upper[1cl* + l3 - e5]
        elif i.islower:
            idx = lower.find(i)
            if idx + 13 <= 25:
                result += lower[idx + 13]
            else:
                result += lower[idx + 13 - 25]
    else:
        result += i
print(result)