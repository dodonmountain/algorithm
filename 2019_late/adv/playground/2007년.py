cal = {
    1: 31,
    2: 28,
    3: 31,
    5: 31,
    7: 31,
    8: 31,
    10: 31,
    12: 31,
    4: 30,
    6: 30,
    9: 30,
    11: 30
}
week = {
    1: 'MON',
    2: 'TUE',
    3: 'WED',
    4: 'THU',
    5: 'FRI',
    6: 'SAT',
    0: 'SUN',
}
mon, day = map(int, input().split())

for i in range(1, mon):
    day += cal[i]

print(week[day % 7])
