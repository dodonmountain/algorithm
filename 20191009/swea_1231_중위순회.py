import sys;sys.stdin=open('1231.txt')

def inorder(v):
    global answer
    if v == 0: return
    inorder(L[v])
    answer += words[v]
    inorder(R[v])
    
for t_case in range(1, 11):
    V = int(input())
    E = V - 1
    L = [0] * (V+1)
    R = [0] * (V+1)
    words = ['0']
    for i in range(1, V+1):
        arr = list(input().split())
        if len(arr) == 4:
            p, w, l, r = int(arr[0]), arr[1], int(arr[2]), int(arr[3])
        elif len(arr) == 3:
            p, w, l, r = int(arr[0]), arr[1], int(arr[2]), 0
        else:
            p, w, l, r = int(arr[0]), arr[1], 0, 0
        L[p], R[p] = l, r
        words.append(w)
    answer = ''
    inorder(1)
    print("#{} {}".format(t_case, answer))