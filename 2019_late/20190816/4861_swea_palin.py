import sys
sys.stdin = open('input.txt')

T = int(input())
for t_case in range(T):
    N, M = map(int, input().split())
    board = [] # 가로
    for lines in range(N):
        board.append(input())
    board_rotate = []
    for i in range(N):
        tmp = ''
        for j in range(N):
            tmp += board[j][i]
        board_rotate.append(tmp)
    for j in range(N): # 줄 수만큼
        for i in range(N - M + 1): # 글자 수 - 회문 체크 길이만큼
            if board[j][i:i + M] == board[j][i:i + M:][::-1]:
                print('#{} {}'.format(t_case + 1, board[j][i:i + M]))
            elif board_rotate[j][i:i + M] == board_rotate[j][i:i + M:][::-1]:
                print('#{} {}'.format(t_case + 1, board_rotate[j][i:i + M]))





