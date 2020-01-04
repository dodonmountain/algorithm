from itertools import permutations as pm
import math
T = int(input())
for t_case in range(T):

    N = int(input())
    res = math.factorial(N)
    all = pm(range(1,N+1))
    for board in all:
        diag = []
        flag, flag2 = True, True
        tmp = -1
        for idx, row in enumerate(board):
            if tmp + 1 == row:
                if tmp -1 == row:
                    flag2 = False
            tmp = row
            if flag2:
                for c in range(len(diag)):
                    if abs(diag[c]-row) == abs(c-idx):
                        flag = False
                        break
                    flag = True
            if flag:
                diag.append(row)
            else:
                res -= 1
                break
    print("#{} {}".format(t_case+1, res))