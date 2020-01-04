import sys
sys.stdin = open('input.txt')

qt = int(input())
now = list(map(int, input().split()))
students = int(input())


def click(digit):
    if digit == 0:
        return 1
    else:
        return 0


for cases in range(students):
    gender, number = map(int, input().split())
    # 스위치 조작
    if gender == 1:    # 남학생 조작
        for i in range(len(now)):
            if (i+1) % number == 0:
                now[i] = click(now[i])
    elif gender == 2: # 여학생 조작
        j = 0
        center = number - 1
        while True:
            if number == 1:
                break
            elif number == qt:
                break
            elif center + j == len(now):
                break
            elif center - j < 0:
                break
            elif now[center + j] != now[center - j]:
                break
            else:
                now[center + j] = click(now[center + j])
                now[center - j] = click(now[center - j])
                j += 1
        now[center] = click(now[center])

for cnt in range(qt):
    if cnt % 20 == 0 and cnt != 0:
        print()
    print(now[cnt], end=' ')
print()
