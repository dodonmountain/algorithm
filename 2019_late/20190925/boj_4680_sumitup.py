import sys;sys.stdin = open('4680.txt')

def solve(s, d, lst):
    global res
    if s > t:
        return
    if d == N:
        if s == t:
            if lst not in res:
                res.append(lst)
        return
    solve(s + arr[d], d + 1, lst+[arr[d]])
    solve(s, d + 1, lst)
while True:
    arr = list(map(int, input().split()))
    if arr == [0, 0]:break
    t = arr.pop(0); N = arr.pop(0)
    res = []
    solve(0,0,[])
    print('Sums of {}:'.format(t))
    if res:
        for i in range(len(res)):
            print(*res[i],sep='+')
    else:
        print('NONE')