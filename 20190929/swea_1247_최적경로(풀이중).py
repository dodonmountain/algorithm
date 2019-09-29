import sys; sys.stdin = open('1247.txt')

def solve(s, d, dt):
    if d == N:
        print(*s)
        return
    for i in range(N):
        if not used[i]:
            s.append(i)
            used[i] = 1
            customer[i][0] customer[i][1]
            solve(s, d+1, dt)
            used[i] = 0
            s.pop()


T = int(input())
T =1 
for t_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    company = [arr.pop(0), arr.pop(0)]
    home = [arr.pop(0), arr.pop(0)]
    customer = []
    for i in range(len(arr)):
        if not i & 1:
            customer.append([arr[i], arr[i+1]])
    used = [0] * N
    solve([], 0, 0)