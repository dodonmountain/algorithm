import sys
sys.stdin = open('5201.txt')

for t_case in range(int(input())):
    n, m = map(int, input().split())
    wght = sorted(list(map(int, input().split())))
    truck = sorted(list(map(int, input().split())))
    res, used = 0, [0] * (m+1)
    while wght:
        cargo = wght.pop(-1)
        for i in range(m):
            if truck[i] >= cargo and not used[i]:
                res += cargo
                used[i] = 1
                break
    print('#{} {}'.format(t_case+1, res))



    