import sys
sys.stdin = open('input.txt')

for t_case in range(10):
    N = int(input())
    board = []  # 가로
    cnt = 0
    for lines in range(8):
        board.append(input())
    board_rotate = []
    for i in range(8):
        tmp = ''
        for j in range(8):
            tmp += board[j][i]
        board_rotate.append(tmp)
    for j in range(8):  # 줄 수만큼
        for i in range(8 - N + 1):  # 글자 수 - 회문 체크 길이만큼
            if board[j][i:i + N] == board[j][i:i + N:][::-1]:
                cnt += 1
    for j in range(8):  # 줄 수만큼
        for i in range(8 - N + 1):  # 글자 수 - 회문 체크 길이만큼
            if board_rotate[j][i:i + N] == board_rotate[j][i:i + N:][::-1]:
                cnt += 1
    print('#{} {}'.format(t_case + 1, cnt))