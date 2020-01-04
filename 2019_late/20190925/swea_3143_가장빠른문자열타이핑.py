import sys
sys.stdin = open('3143.txt')

for t_case in range(int(input())):
    a, b = input().split()
    res = len(a) - (len(b) * a.count(b)) + a.count(b)
    print('#{} {}'.format(t_case+1, res))
    