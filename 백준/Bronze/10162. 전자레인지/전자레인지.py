T = int(input())

buttons = [0, 0, 0]

while T:
    if T >= 300:
        buttons[0] += 1
        T -= 300
    elif T >= 60:
        buttons[1] += 1
        T -= 60
    elif T >= 10:
        buttons[2] += 1
        T -= 10
    else:
        print(-1)
        break

if T == 0:
    print(*buttons)