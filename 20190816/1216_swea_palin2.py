import sys
sys.stdin = open('input.txt')


for t_case in range(10):
    trash = int(input())
    board = []  # 가로
    for lines in range(100):
        board.append(input())
    board_rotate = []
    for i in range(100):
        tmp = ''
        for j in range(100):
            tmp += board[j][i]
        board_rotate.append(tmp)
    #     가로
    longest = ''
    N = 1
    while True:
        if N > 99:
            break
        for j in range(100):  # 줄 수만큼
            for i in range(100 - N + 1):  # 글자 수 - 회문 체크 길이만큼
                if board[j][i:i + N] == board[j][i:i + N:][::-1]:
                    if len(board[j][i:i + N]) > len(longest):
                        longest = board[j][i:i + N]
        for j in range(100):  # 줄 수만큼
            for i in range(100 - N + 1):  # 글자 수 - 회문 체크 길이만큼
                if board_rotate[j][i:i + N] == board_rotate[j][i:i + N:][::-1]:
                    if len(board[j][i:i + N]) > len(longest):
                        longest = board[j][i:i + N]
        N += 1
    print('#{} {}'.format(t_case + 1, len(longest)))