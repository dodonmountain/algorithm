import sys
sys.stdin = open('5688.txt')
for t_case in range(int(input())):
    N = int(input())
    flag = False
    for i in range(int(N**0.333333333)+2):
        if i ** 3 == N:
            res = i
            flag = True
            break
    if flag:
        print('#{} {}'.format(t_case+1, res))
    else:
        print('#{} {}'.format(t_case+1, -1))