import sys;sys.stdin=open('boj1149.txt')

def solve(d, cost, prev):
    global answer
    if d == N:
        answer = min(answer, cost)
        return
    for i in range(3):
        if i != prev:
            solve(d + 1, cost + street[d][i], i)
        

N = int(input())
street = [list(map(int, input().split())) for _ in range(N)]
answer = 1000000
solve(0, 0, 3)
print(answer)