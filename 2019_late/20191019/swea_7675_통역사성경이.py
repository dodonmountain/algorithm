import sys;sys.stdin = open('7675.txt')

T = int(input())

for t_case in range(T):
    print('#{}'.format(t_case+1),end=' ')
    N = int(input())
    arr = list(input().split())
    cnt = 0
    for word in arr:
        if word[-1] in '!.?':
            if word[0].isupper():
                flag = True
                for i in range(1, len(word)-1):
                    if word[i].islower():
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    cnt += 1
            print(cnt, end=' ')
            cnt = 0
        else:
            if word[0].isupper():
                flag = True
                for i in range(1, len(word)):
                    if word[i].islower():
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    cnt += 1
    print()