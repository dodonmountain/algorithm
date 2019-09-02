import sys
sys.stdin = open('5110.txt')
from collections import deque
T = int(input())

for t_case in range(T):
    N, M = map(int, input().split())
    lst = deque()
    result = deque()
    for _ in range(M):
        lst.append(deque(map(int,input().split())))
    res = deque()
    res.extend(lst.popleft())
    maxnow = max(res)
    for i in lst:
        if maxnow > i[0]:
            for s in range(len(res)):
                if res[s] > i[0]:
                    break
            tmp = len(res)-s
            res.rotate(tmp)
            res.extend(i)
            res.rotate(-tmp)
        else:
            res.extend(i)
        if maxnow < max(i):
            maxnow = max(i)
    for i in range(1, 11):
        result.append(str(res[-i]))
    print("#{} {}".format(t_case + 1, ' '.join(result)))