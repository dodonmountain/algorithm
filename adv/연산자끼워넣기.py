def solve(s, d, ops):
    global mx, mn
    if d == N:
        if s < mn:mn = s
        if s > mx:mx = s
        return
    for i in range(4):
        if ops[i] > 0:
            ops[i] -= 1
            if i == 0:
                solve(s + arr[d], d + 1, ops)
            elif i == 1:
                solve(s - arr[d], d + 1, ops)
            elif i == 2:
                solve(s * arr[d], d + 1, ops)
            elif i == 3:
                solve(int(s / arr[d]), d + 1, ops)
            ops[i] += 1

N = int(input())
arr = list(map(int, input().split()))
ops = list(map(int, input().split()))
mx, mn = -9999999999, 0x999999999
solve(arr[0], 1, ops)
print(mx)
print(mn)