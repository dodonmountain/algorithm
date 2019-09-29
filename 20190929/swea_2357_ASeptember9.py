def div(num):
    while num:
        if num % 10 == 9:
            return False
        num //= 10
    return True

for t_case in range(int(input())):
    N = int(input())
    if div(N):
        answer = 'No'
    else:
        answer = 'Yes'
    print(f'#{t_case+1} {answer}')