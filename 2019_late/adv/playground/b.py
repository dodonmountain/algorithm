superset = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]

superset = lambda x: [[y for i, y in en]]