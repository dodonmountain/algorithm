import sys
sys.stdin = open('15820.txt')
flag = True
s1, s2 = map(int, input().split())
for i in range(s1):
    a ,b = map(int, input().split())
    if a != b:
        flag = False
        print('Wrong Answer')
        break
if flag:
    for j in range(s2):
        a ,b = map(int, input().split())
        if a != b:
            flag = False
            print('Why Wrong!!!')
            break
if flag:
    print('Accepted')