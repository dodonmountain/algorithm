import sys
sys.stdin = open('5120.txt')


from collections import deque

T = int(input())

for t_case in range(T):
    res = []
    N, M, K = map(int, input().split())
    pword = deque(map(int, input().split()))
    start = 0
    for i in range(K):
        print(pword)
        pword.rotate(-M)
        a = pword[0]
        b = pword[-1]
        pword.appendleft(a+b)
    pword.rotate(K)

    i = 1
    while len(res) < 11 and i < len(pword)+1:
        res.append(str(pword[-i]))
        i += 1
    print("#{} {}".format(t_case+1, ' '.join(res)))












    # for i in range(K):
        # if start + M >= len(pword):
        #     prev = start
        #     start = len(pword) - start - 1
        # else:
        #     prev = start
        #     start = start + M
        # if start == 0:
        #     pword.appendleft(pword[0] + pword[prev])
        # elif start == len(pword)-1:
        #     pword.append(pword[-1]+pword[prev])
        # else:
        # pword.insert(start, pword[start-1]+ pword[start] )

