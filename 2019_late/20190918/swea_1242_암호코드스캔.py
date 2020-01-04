import sys
sys.stdin = open('1242.txt')

T = int(input())

for t_case in range(T):
    N, M = map(int, input().split())
    arr = [list(list(input())) for _ in range(N)]
    for y in range(N-1,-1,-1):
        for x in range(M-1,-1,-1):
            if arr[y][x] != '0':
                break
        if arr[y][x] != '0':
            break



        
    decoder = [
        [0,0,0,1,1,0,1],
        [0,0,1,1,0,0,1],
        [0,0,1,0,0,1,1],
        [0,1,1,1,1,0,1],
        [0,1,0,0,0,1,1],
        [0,1,1,0,0,0,1],
        [0,1,0,1,1,1,1],
        [0,1,1,1,0,1,1],
        [0,1,1,0,1,1,1],
        [0,0,0,1,0,1,1]
    ]
    for i in range(M - x):
        if arr[y][x-i] 
    code = []
    for i in range(0, 56, 7):
        code.append(arr[y][x-6-i:x+1-i])
    code = code[::-1]
    for i in range(8):
        for s in range(10):
            if code[i] == decoder[s]:
                code[i] = s
                break
    tmp1,tmp2 = 0,0
    for i in range(7):
        if not i % 2:
            tmp1 += code[i]
        else:
            tmp2 += code[i]
    if not (((tmp1*3) + tmp2) +code[-1]) % 10:
        valid = True
    else:
        valid = False
    if valid:
        print('#{} {}'.format(t_case+1, sum(code)))
    else:
        print('#{} {}'.format(t_case+1, 0))
