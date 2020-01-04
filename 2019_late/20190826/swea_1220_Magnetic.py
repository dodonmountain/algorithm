import sys
sys.stdin = open("input1220.txt")
from pprint import pprint
T = 10

for t_case in range(T):
    N = int(input())
    board, check = [],[]
    cnt = 0
    for i in range(100):
        board.append(list(map(int, input().split())))
    for i in range(100):
        for j in range(100):
            if board[j][i] != 0:
                check.append(board[j][i])

        # 남쪽으로 떨어질 친구들 치우기
        for c in range(len(check)-1,-1,-1):
            if check[c] == 1:
                check.pop(c)
            else:
                break
        check = check[::-1]
        # 북쪽으로 떨어질 친구들도 치우기
        for c in range(len(check)-1, -1, -1):
            if check[c] == 2:
                check.pop(c)
            else:
                break
        check = check[::-1]
        for c in range(len(check) - 1, -1, -1):
            if check[c] == check[c - 1]:
                check.pop(c)
    print("#{} {}".format(t_case+1, len(check)//2))
