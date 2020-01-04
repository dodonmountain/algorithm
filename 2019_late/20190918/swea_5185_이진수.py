import sys
sys.stdin = open('5185.txt')

T = int(input())

for t_case in range(T):
    N, arr = input().split()
    N = int(N)
    l = len(arr) * 4
    arr = int('0x' + arr, 16)
    ll = l - len(str(bin(arr).lstrip('0b')))
    res = '0'*ll+str(bin(arr).lstrip('0b'))
    print('#{} {}'.format(t_case + 1, res))
