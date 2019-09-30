import sys; sys.stdin = open('6959.txt')

for t_case in range(int(input())):
    num = list(input())
    turn = 0
    while len(num) > 1:
        a = num.pop()
        b = num.pop()
        num.extend(list(str(int(a) + int(b))))
        turn += 1
    if turn & 1:
        print('#{} A'.format(t_case+1))
    else:
        print('#{} B'.format(t_case+1))