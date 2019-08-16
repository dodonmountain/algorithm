import sys
sys.stdin = open('input.txt')

T = int(input())
for t_case in range(T):
    N = int(input())
    hotel = {x:0 for x in range(1, 401)}
    for tasks in range(N):
        now, home = map(int, input().split())
        if home % 2:
            home = home + 1
        for i in range(abs(home - now) + 1):
            if home > now:
                hotel[now + i] += 1
            elif home < now:
                hotel[now - i] += 1
    print('#{} {}'.format(t_case+1, max(hotel.values())))