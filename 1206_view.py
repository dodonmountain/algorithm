t_case = 10
for t in range(t_case):
    test = int(input())
    stories = list(map(int, input().split()))
    result = 0
    for i in range(test):
        if stories[i] > 0:
            mh1 = stories[i - 1] if stories[i - 1] > stories[i - 2] else stories[i - 2]
            mh2 = stories[i + 1] if stories[i + 1] > stories[i + 2] else stories[i + 2]
            max_height = mh1 if mh1 > mh2 else mh2
            result += stories[i] - max_height if stories[i] - max_height > 0 else 0

    print('#{} {}'.format(t + 1, result))