import sys;sys.stdin=open('1248.txt')

tc = input()
for t_case in range(1):
    v, e, a, b = map(int, input().split())
    arr = list(map(int, input().split()))
    T = [[] for _ in range(v+1)]
    for i in range(0, 2 * e, 2):
        T[arr[i]].append(arr[i+1])
    print(T)