
def gcd(a, b):
    while b:
        r = a % b
        a, b = b, r
    return a

a, b = map(int, input().split())
_gcd = gcd(a, b)
print(_gcd)
print(int(a * b / _gcd))
