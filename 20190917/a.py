from sys import getsizeof
a = [i for i in range(10000000)]
b = (i for i in range(10000000))
c = {i:0 for i in range(10000000)}
d = set(i for i in range(10000000))
e = range(10000000)
print(getsizeof(a),getsizeof(b),getsizeof(c),getsizeof(d), getsizeof(e))