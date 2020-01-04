
for t_case in range(10):
    T = int(input())
    lst = [list(map(int, input().split())) for _ in range(100)]
    res = []
    # 가로
    for i in range(100):
        res.append(sum(lst[i]))
    # 세로
    for i in range(100):
        tmp = 0
        for j in range(100):
            tmp += lst[j][i]
        res.append(tmp)
    tmp = 0
    # 대각선
    for i in range(100):
        tmp += lst[i][i]
    res.append(tmp)
    tmp = 0
    # 반대대각선
    for i in range(99, 0, -1):
        tmp += lst[i][i]
    res.append(tmp)
    print('#{} {}'.format(t_case+1, max(res)))