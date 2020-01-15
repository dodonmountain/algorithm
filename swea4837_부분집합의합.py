superset = lambda x: [(len([y for j, y in enumerate(set(x)) if (i >> j) & 1]), sum([y for j, y in enumerate(set(x)) if (i >> j) & 1])) for i in range(2**len(set(x)))]
arr = superset(range(1, 13))
for tc in range(int(input())):
    n, k = map(int, input().split());cnt = 0
    for j in arr:
        if j[0] == n and j[1] == k:cnt += 1
    print(f'#{tc+1} {cnt}')

