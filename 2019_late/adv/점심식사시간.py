from collections import deque
from pprint import pprint
import sys
sys.stdin = open('lunch.txt')


def comp(array, whichStair):
    s = array[::]
    time = 0
    entrance = []
    down = []
    cnt = 0
    population = len(s)
    if len(s) == 1:
        return s[0] + 1 + stair[whichStair][2]
    elif s:
        while cnt < population:
            time += 1
            # 1분 경과
            if entrance:
                for i in range(len(entrance)-1, -1, -1):
                    if entrance[i] == 1:
                        entrance[i] = 0
                    else:
                        if len(down) < 3:  # 내려가는 인원이 세명보다 적다면
                            entrance.pop(i)
                            down.append(stair[whichStair][2])
            for i in range(len(down)-1, -1, -1):
                down[i] -= 1
                if down[i] == 0:
                    down.pop(i)
                    cnt += 1
            if s[-1] > -1:
                for i in range(len(s)):
                    # 입구까지 간다
                    s[i] -= 1
                    if s[i] == 0:
                        # 만약 입구라면
                        entrance.append(1)
                        # 입구에 1분을 넣는다.
    return time


def solve(d, s1, s2):
    if d == len(people):
        s1.sort()
        s2.sort()
        com(s1, s2)
        return (s1, s2)
    solve(d+1, s1 + [people[d][2]], s2)
    solve(d+1, s1, s2 + [people[d][3]])


def com(s1, s2):
    global minnow
    # print(s1,s2)
    t1 = comp(s1, 0)
    t2 = comp(s2, 1)
    if max((t1, t2)) < minnow:
        minnow=max((t1, t2))
    # print(minnow)
    return

T=int(input())
T = 10
for tc in range(T):
    N=int(input())
    board=[list(map(int, input().split())) for _ in range(N)]
    people=[]
    stair=[]
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                if board[i][j] > 1:
                    stair.append((i, j, board[i][j]))
                else:
                    people.append([i, j])
    for person in people:
        person.append(abs(stair[0][0] - person[0])+abs(stair[0][1] - person[1]))
        person.append(abs(stair[1][0] - person[0])+abs(stair[1][1] - person[1]))
    minnow=0x999999
    # print(people)
    solve(0, [], [])
    print('#{} {}'.format(tc+1, minnow))
