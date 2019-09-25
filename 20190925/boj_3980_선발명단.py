import sys
sys.stdin = open('3980.txt')

def solve(s, d):
    global tmp
    if d == 11:
        if s > tmp:
            tmp = s
        return
    for pos in range(11):
        if not position[pos]:
            if board[d][pos]:
                position[pos] = 1
                solve(s+board[d][pos], d+1)
                position[pos] = 0

for t_case in range(int(input())):
    board = [list(map(int, input().split())) for _ in range(11)]
    position = [0] * 11;tmp = 0
    solve(0, 0)
    print(tmp)