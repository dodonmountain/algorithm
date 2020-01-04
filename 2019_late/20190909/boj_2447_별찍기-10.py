
# 3 ** 9 = 19683



def star(x, y, max, matrix):
    if max == 1:
        matrix[x][y] = '*'
        return
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                pass
            else:
                star(x + (i * (max // 3)), y + (j * (max // 3)), max//3 , matrix)
N = int(input())
matrix = [[' '] * 2187 for _ in range(2187)]
star(0, 0, N, matrix)
for i in range(N):
    answer = ''
    for j in range(N):
        answer += matrix[i][j]
    print(answer)