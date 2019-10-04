def made(num):
    multiplier = num % 10
    num //= 10
    return num ** multiplier
 
for t_case in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    print('#{} {}'.format(t_case+1, sum(map(made, arr))))
