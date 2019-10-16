import sys;sys.stdin=open('5174.txt')

def treeSize(v):
    global t_size
    if v == 0:return
    t_size += 1
    treeSize(L[v])
    treeSize(R[v])

for t_case in range(int(input())):
    E, N = map(int, input().split())
    V = E + 1
    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)
    arr = list(map(int, input().split()))
    for i in range(0, 2*E, 2):
        if L[arr[i]]:
            R[arr[i]] = arr[i+1]
        else:
            L[arr[i]] = arr[i+1]
    t_size = 0 
    treeSize(N)
    print('#{} {}'.format(t_case+1, t_size))
