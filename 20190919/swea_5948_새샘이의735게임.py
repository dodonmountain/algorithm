import sys
sys.stdin = open('5948.txt')

T = int(input())

def solve(s):
    global perm
    if len(s) == 3:
        perm.append(sum(s))
        return
    else:
        for k in range(6,-1,-1):
            if used[k]:
                maxnow = k
                break
            maxnow = 0
        for i in range(maxnow, 7):
            if not used[i]:
                used[i] = 1
                s.append(arr[i])
                solve(s)
                s.pop()
                used[i] = 0
for t_case in range(T):
    arr = list(map(int, input().split()))
    arr.sort()
    used = [0] * 7
    perm = []
    solve([])
    perm = sorted(list(set(perm)),reverse=True)
    print('#{} {}'.format(t_case+1, perm[4]))