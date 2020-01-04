def back(b,c):
    global tmp
    if b == c:
        return 
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
            tmp += 1
            return
    else:
        for i in range(1, N + 1):
            if not used[i]:
                used[i] = i
                b.append(i)
                back(b,c+1)
                used[i] = 0
                b.pop()

N = int(input())
used = [0] * (N+1)
tmp = 0
back([],0)
print(tmp)
