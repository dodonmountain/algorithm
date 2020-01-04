import sys
sys.stdin = open('3975.txt')


arr = ['ALICE','BOB','DRAW']
T = int(input())
cod = []
for t_case in range(T):
    a,b,c,d  = map(int, input().split())
    f = (a / b) - (c / d)
    if f > 0:
        cod.append(0)
    elif f < 0:
        cod.append(1)
    else:
        cod.append(2)
for i in range(T):
    print('#{} {}'.format(i+1, arr[cod[i]]))