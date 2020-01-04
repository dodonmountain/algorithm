import sys;sys.stdin=open('1233.txt')


def trav(v):
    if len(tree[v]) == 4:
        if tree[v][1] == '+':
            return trav(tree[v][2]) + trav(tree[v][3])
        elif tree[v][1] == '-':
            return trav(tree[v][2]) - trav(tree[v][3])
        elif tree[v][1] == '*':
            return trav(tree[v][2]) * trav(tree[v][3])
        elif tree[v][1] == '/':
            return trav(tree[v][2]) // trav(tree[v][3])
    elif len(tree[v]) == 2:
        return tree[v][1]

for t_case in range(10):
    N = int(input())
    tree = [[0]]
    for i in range(N):
        arr = list(input().split())
        if len(arr) == 4:
            tree.append([int(arr[0]), arr[1], int(arr[2]), int(arr[3])])
        else:
            tree.append([int(arr[0]), int(arr[1])])
    print('#{} {}'.format(t_case+1, trav(1)))