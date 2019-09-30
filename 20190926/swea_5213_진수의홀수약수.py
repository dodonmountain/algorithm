import sys; sys.stdin = open('5213.txt')

table = [0] * (1000002)
table2 = [0] * (1000002)
for i in range(1,1000001):
    for j in range(1, (1000001//i)+1, 2):
        table[i*j] += j
for i in range(1, 1000001):
    table2[i] = table2[i-1] + table[i]
for t_case in range(int(input())):
    L, R = map(int, input().split())
    answer = table2[R] - table2[L-1]
    print('#{} {}'.format(t_case+1, answer))