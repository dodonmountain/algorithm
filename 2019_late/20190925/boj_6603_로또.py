import sys
sys.stdin = open('6603.txt')
def solve(r, d):
    if len(r) == 6:
        print(*r)
        return
    mxn = 0
    for j in range(len(used)-1,-1,-1):
        if used[j] != 0:
            mxn = j+1
            break
    for i in range(mxn, k):
        if not used[i]:
            r.append(arr[i])
            used[i] = 1
            solve(r, d+1)
            used[i] = 0
            r.pop()

while True:
    a = input()
    if a == '0': break
    arr = list(map(int, list(a.split()))); k = arr.pop(0)
    used = [0] * (k + 1)
    solve([], 0)
    print()

