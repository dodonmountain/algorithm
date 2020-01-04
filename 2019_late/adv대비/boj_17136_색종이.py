import sys
sys.stdin = open('17136.txt')
from pprint import pprint
def checker(y, x, size):
    for yy in range(y, y + size):
        for xx in range(x, x + size):
            if -1 < yy < 10 and -1 < xx < 10:
                if board[yy][xx] == 0:
                    return 0
            else:
                return 0
    return 1
def checkerr(y, x, size):
    for yy in range(y, y + size):
        for xx in range(x, x + size):
            if -1 < yy < 10 and -1 < xx < 10:
                if brev[yy][xx] == 0 and checkr[yy][xx] == '□':
                    return 0
            else:
                return 0
    return 1
def checked(y, x, size):
    for yy in range(y + size, y ):
        for xx in range(x + size, x):
            check[yy][xx] = str(size)
def checkedr(y, x, size):
    for yy in range(y, y + size):
        for xx in range(x, x + size):
            checkr[yy][xx] = str(size)
board, brev = [], []
for _ in range(10):
    aaaa = list(map(int,input().split()))
    board.append(aaaa)
    brev.append(aaaa[::-1])
brev = brev[::-1]
papers = [0, 0, 0, 0, 0, 0]
papersr = [0, 0, 0, 0, 0, 0]
check = [['□'] * 10 for _ in range(10)]
checkr = [['□'] * 10 for _ in range(10)]
def main(big):
    global papers, papers, check, checkr
    papers = [0, 0, 0, 0, 0, 0]
    papersr = [0, 0, 0, 0, 0, 0]
    check = [['□'] * 10 for _ in range(10)]
    checkr = [['□'] * 10 for _ in range(10)]
    for i in range(10):
        for j in range(10):
            if check[i][j] == '□':
                for k in range(big, 0,-1):
                    if checker(i, j, k):
                        papers[k] += 1
                        checked(i,j,k)
                        break
            if checkr[i][j] == '□':
                for k in range(big, 0,-1):
                    if checkerr(i, j, k):
                        papersr[k] += 1
                        checkedr(i,j,k)
                        break
    result = []
    pprint(checkr)
    result.append(sum(papers))
    result.append(sum(papersr))
    for cc in range(6):
        if papers[cc] > 5:
            result[0] = 99999
        if papersr[cc] > 5:
            result[1] = 99999
    if min(result) == 99999:
        return -1
    else:
        return min(result)

final = []
for i in range(1,6):
    if main(i) != -1:
        final.append(main(i))
if final == []:
    print(-1)
else:
    print(min(final))