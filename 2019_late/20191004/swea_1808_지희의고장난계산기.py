import sys;sys.stdin = open('1808.txt')

def check(num):
    while num:
        if num % 10 not in usable:
            return 0
        num //= 10
    return 1

def my_len(num):
    cnt = 0
    while num:
        num //= 10
        cnt += 1
    return cnt 

def make_div(num):
    div = []
    for i in range(int(num**0.5), 1, -1):
        if num % i == 0:
            k = num // i
            if check(k):
                div.append((k, my_len(k) + 1))
            if check(i):
                div.append((i, my_len(i) + 1))
    return div

def back(s, d):
    global answer
    if s == X:
        if answer > d:
            answer = d
        return
    for i in table:
        if s * i[0] <= X:
            back(s * i[0], d + i[1])
for t_case in range(1, int(input()) + 1):
    arr = list(map(int, input().split()))
    X = int(input())
    usable = set()
    for i in range(10):
        if arr[i]:usable.add(i)
    if check(X):answer = my_len(X) + 1
    else:
        table, answer = make_div(X), 128
        print(table)
        for i in table:
           back(i[0], i[1])
        if answer == 128:answer = -1
    print('#{} {}'.format(t_case, answer))