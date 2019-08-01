T = int(input())
for t_cases in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    #     ==
    t_max = lst[0]
    t_min = lst[0]
    for numbers in lst:
        if numbers > t_max:
            t_max = numbers
        elif numbers < t_min:
            t_min = numbers
    print('#{} {}'.format(t_cases+1, t_max - t_min))