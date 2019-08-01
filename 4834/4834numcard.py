T = int(input())
for t_case in range(1, T + 1):
    N = int(input())
    counter = [0] * 10
    lst = list(map(int, list(input())))
    tmp = counter[0]
    num = 0
    for i in lst:
        counter[i] += 1

    for i in range(10):
        if counter[i] >= tmp:
            tmp = counter[i]
            num = i
    print('#{} {} {}'.format(t_case, num, tmp))
