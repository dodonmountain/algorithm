import sys
input = sys.stdin.readline
bingo = [list(map(int, input().split())) for _ in range(5)]
given = []
for _ in range(5):
    given += (list(map(int, input().split())))

checker = [[0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0],
           [0,0,0,0,0]]

def bi_3(arr):

    bc = 0
    for k in range(5):
        if sum(arr[k]) == 5:
            bc += 1
    for k in range(5):
        if checker[0][k]+checker[1][k]+checker[2][k]+checker[3][k]+checker[4][k] == 5:
            bc += 1
    if checker[0][0] + checker[1][1] + checker[2][2] + checker[3][3] + checker[4][4] == 5:
        bc += 1
    if checker[0][4] + checker[1][3] + checker[2][2] + checker[3][1] + checker[4][0] == 5:
        bc += 1
    return bc

for count in range(len(given)):

    if bi_3(checker) > 2:
        print(count)
        break
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == given[count]:
                checker[i][j] = 1

