"""
5*5 2차 배열에 무작위로 25개의 숫자로 초기화 한 후
25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값을 구하시오.
예를 들어 아래 그림에서 7값의 이웃한 값은 26812이며 차의 절대값의 합은 12이다.
2-7 + 6-7 + 8-7 + 12-7 = 12

... 2 ...
 6  7  8
...12 ...
"""

arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]

N, M = len(arr) , len(arr[0])

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for x in range(N):
    for y in range(M):
        for i in range(len(dx)):
            tx, ty = x + dx[i], y + dy[i]
            if tx == 0 or tx < 0 or ty == 0 or ty < 0:
                # 모서리
            else:
                print(abs(arr[x][y] - arr[tx][ty]))