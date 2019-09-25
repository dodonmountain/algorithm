def pascal(n):
    for i in range (n):
        k = 1
        arr = [k]
        for j in range(i):
            k = k * ( i - j ) * 1 / ( j + 1 )
            arr.append(int(k))
        print(*arr)

for t_case in range(int(input())):
    N = int(input())
    print('#{}'.format(t_case+1))
    pascal(N)