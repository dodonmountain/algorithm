C = [[] * 999 for _ in range(999)]
P = [] * 999


C[30].extend([54,2,45])
C[54].append(1)
C[45].append(123)
visit = [0] * 1000
def trav(v):
    visit[v] = 1
    zrs = 3 - len(str(v))
    print('[{}{}]'.format(zrs*'0',v),end='')
    if not C[v]:
        print()
    
    for w in C[v]:
        if not C[w]:
            print('-----',end='')
        if not visit[w]:
            trav(w)
trav(30)