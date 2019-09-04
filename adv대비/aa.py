def back(choice):
    if len(choice) == 3:
        print(*choice)
    else:
        for i in range(1,6):
            if not used[i]:
                used[i] = 1
                choice.append(i)
                back(choice)
                used[i] = 0
                choice.pop()


numbers = list(range(1, 6))
used = [0]*6
back([])