import sys;sys.stdin = open('3289.txt')
# 유니온 파인드

def uni(p, q):
    p = find(p)
    q = find(q)
    if p == q:return
    parent[q] = p

def find(p):
    if parent[p] == p:
        return p
    parent[p] = find(parent[p])
    return parent[p]

for t_case in range(int(input())):
    n, m = map(int, input().split())
    parent = [i for i in range(n+1)]
    answer = ''
    for i in range(m):
        c, a, b = map(int, input().split())
        if c == 0:
            uni(a, b)
        else:
            aa, bb = find(a), find(b)
            if aa == bb:
                answer += '1'
            else:
                answer += '0'
    print('#{} {}'.format(t_case+1, answer))
