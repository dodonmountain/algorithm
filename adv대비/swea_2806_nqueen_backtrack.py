import sys
sys.stdin = open('2806.txt')


T = int(input())
def back(b,c,all):
    if c > 1:
        if abs(b[-1] - b[-2]) == 1:
            return
    if c >= N:
        flag = True
        for k in range(len(b)):
            for l in range(k+1, len(b)):
                if abs(b[k] - b[l]) == abs(k - l):
                    flag = False
        if flag:
            all.append([*b])
            return
    else:
        for i in range(1, N + 1):
            if not used[i]:
                used[i] = i
                b.append(i)
                back(b,c+1,all)
                used[i] = 0
                b.pop()

for t_case in range(T):
    N = int(input())
    used = [0] * (N+1)
    all = []
    back([],0,all)
    print("#{} {}".format(t_case + 1, len(all)))