import itertools

lst = (1,2,4)
res = ()
for i in range(9):
    res += tuple(itertools.product(lst, repeat=i))
print(list(map(''.join, res[5])))
