N, S = map(int, input().split())
arr = sorted(list(map(int, input().split())))
superset = lambda x: [[y for j, y in enumerate((x)) if (i >> j) & 1] for i in range(2**len((x)))]
cnt = 0

for i in superset(arr)[1:]:
    if sum(i) == S:
        cnt += 1
print(cnt)