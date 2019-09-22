import sys
sys.stdin = open('14501.txt')

def solve(day, p):
    global tmp
    if day >= N:
        if day == N:
            if time[day] == 1:
                p += pay[day]
        if p > tmp:
            tmp = p
        return
    if not day + time[day] > N + 1:
        solve(day + time[day], p + pay[day])
    solve(day + 1, p)

N = int(input())
time, pay = [0], [0]
for i in range(N):
    t, c = map(int, input().split())
    time.append(t), pay.append(c)
tmp = 0
solve(1, 0)
print(tmp)
