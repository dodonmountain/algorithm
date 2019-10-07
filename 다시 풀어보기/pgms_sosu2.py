import itertools
def ipr(num):
    if num <= 1:
        return False
    elif num == 2:
        return True
    elif num % 2 == 0:
        return False
    for i in range(3, int(num**0.5)+1, 2):
        if num % i == 0:
            return False
    return True
numbers = '011'
numbers = list(numbers)
res = set([])
lst = []
for i in range(0, len(numbers)):
    lst += list(map(''.join ,itertools.permutations(numbers,len(numbers)-i)))
for i in lst:
    if ipr(int(i)) == True:
        res.add(int(i))
answer = len(res)
print(answer)
# cnt = 0
# for i in range(1, 1 << len(numbers)):
#     print([numbers[x] for x in range(len(numbers)) if (i & (1 << x))])
#     if ipr(int(''.join([numbers[x] for x in range(len(numbers)) if (i & (1 << x))]))):
#         cnt += 1
