import sys
sys.stdin = open("1970.txt")

T = int(input())

def solve(N):
    if N == 0:
        return
    else:
        for i in counter.keys():
            while i <= N:
                N -= i
                counter[i] += 1
for t_case in range(T):
    N = int(input())
    counter = {50000:0,10000:0,5000:0,1000:0,500:0,100:0,50:0,10:0}
    solve(N)
    print('#{}'.format(t_case+1))
    print(*list(counter.values()))