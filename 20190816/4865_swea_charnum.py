import sys
sys.stdin = open('input.txt')

T = int(input())
for t_case in range(T):
    str_n = set(input())
    d_n = {str_n : 0 for str_n in str_n}
    str_m = input()
    for char in str_m:
        if char in str_n:
            d_n[char] += 1
    print('#{} {}'.format(t_case + 1, max(d_n.values())))


