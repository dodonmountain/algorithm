def back(s):
    if len(s) == 3:
        print(*s)
        return
    else:
        for i in range(1,7):
            if not used[i]:
                used[i] = 1
                s.append(i)
                back(s)
                s.pop()
                used[i] = 0
used = [0]*7
back([])