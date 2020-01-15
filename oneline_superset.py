from functools import reduce
superset_reduce = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])

superset = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]
print(superset([1,2,3,4,5,6]))

superset = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in ragne(2**len(set(x)))]