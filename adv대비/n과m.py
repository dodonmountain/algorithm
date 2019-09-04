# n,m=map(int,input().split())
n,m = 4, 2
from itertools import combinations_with_replacement as cb
print(list(cb(range(1,5),2)))
def back(s,k):
    if len(s) == m:
        print(*s)
        return
    else:
        for i in range(k, n+1):
            s.append(i)
            back(s,i)
            s.pop()

back([],1)
