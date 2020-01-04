T = int(input())
for t_case in range(T):
    str_1 = input()
    str_2 = input()
    if str_1 in str_2:
        print('#{} {}'.format(t_case + 1, 1))
    else:
        print('#{} {}'.format(t_case + 1, 0))