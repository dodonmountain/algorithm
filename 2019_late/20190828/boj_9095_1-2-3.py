T = int(input())
def ott(x):
    print(x)
    if x == n:
        return 1
    elif x > n:
        return 0
    else:
        return ott(x+1) + ott(x+2) + ott(x+3)

for t_case in range(T):
    n = int(input())
    print(ott(0))
