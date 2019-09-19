import sys
sys.stdin = open('1244.txt')

def swop(a,b):
    arr[a], arr[b] = arr[b], arr[a]
    return

def made(a):
    res = 0
    rev = arr[::-1]
    for i in range(L):
        res += rev[i] * 10**i
    return res
        
def solve(k, d):
    global mxtmp
    if d == b:
        res = made(0)
        k.append(res)
        return
    else:
        for i in range(len(arr)):
            for s in range(len(arr)):
                if i != s:
                    if not used[i] and not used[s]:
                        used[i] = 1
                        used[s] = 1
                        swop(s, i)
                        solve(k, d + 1)
                        used[i] = 0
                        used[s] = 0
                        swop(s, i)
                    

T = int(input())

for t_case in range(T):
    a, b = map(int, input().split())
    arr = list(map(int, list(str(a))))
    L = len(arr)
    used = [0] * L
    mxtmp = []
    solve(mxtmp, 0)
    print(max(mxtmp))
