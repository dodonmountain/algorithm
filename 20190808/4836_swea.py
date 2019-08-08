# import sys
# import pprint
# sys.stdin = open("input.txt")

T = int(input())

for t_case in range(T):
    N = int(input())
    area = []
    cnt = 0
    check_area = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    for areas in range(N):
        area.append(list(map(int, input().split())))
    for i in range(N):
        height = area[i][2] - area[i][0]
        width = area[i][3] - area[i][1]
        for h in range(height+1):
            for check in range(width+1):
                check_area[area[i][0]+h][area[i][1] + check ] += area[i][4]


    for k in check_area:
        for kk in k:
            if kk == 3:
                cnt += 1

    print("#{} {}".format(t_case+1, cnt))