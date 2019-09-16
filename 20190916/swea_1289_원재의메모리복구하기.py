import sys
sys.stdin = open('1289.txt')

T = int(input())

def click(s):
    for i in range(len(now) - s):
        if now[s + i]:
            now[s + i] = 0
        else:
            now[s + i] = 1

for t_case in range(T):
    ori = list(map(int, input()))
    now = [0] * len(ori)
    cnt = 0
    for i in range(len(ori)):
        if ori[i] != now[i]:
            click(i)
            cnt += 1
    print('#{} {}'.format(t_case+1, cnt))