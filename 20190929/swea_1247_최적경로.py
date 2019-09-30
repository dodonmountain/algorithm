import sys; sys.stdin = open('1247.txt')



def distance(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def solve(here, dist):
    global tmp
    if sum(visit) == N:
        if tmp > dist + D_home[here]:
            tmp = dist + D_home[here]
        return
    if dist > tmp:
        return
    for i in range(N):
        if not visit[i]:
            visit[i] = 1
            solve(i, dist + D[here][i])
            visit[i] = 0

    

T = int(input())

for t_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    company, home = [arr.pop(0), arr.pop(0)], [arr.pop(0), arr.pop(0)]
    D_company, D_home = [], []
    customer = [[arr[i], arr[i+1]] for i in range(N << 1) if not i & 1 ]
    for i in range(N):
        D_company.append(distance(company, customer[i]))
        D_home.append(distance(home, customer[i]))
    D = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            D[i][j] = distance(customer[i], customer[j])
    visit = [0] * N
    answer = 99999999999
    for i in range(N):
        tmp = 99999999999
        solve(i, D_company[i])
        if tmp < answer:
            answer = tmp
    print('#{} {}'.format(t_case+1, answer))
