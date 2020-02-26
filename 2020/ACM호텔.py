import sys; sys.stdin = open('acm.txt')
from pprint import pprint

def get_room_number(H,W,N,count):
    for j in range(W):
        for i in range(H):
            floor = str(H - (H-1-i))
            room = str(j+1)
            now = floor + '0' + room if int(room) < 10 else floor + room
            count += 1
            if count == N:
                print(now)
                return

for tc in range(int(input())):
    H, W, N = map(int, input().split())
    get_room_number(H,W,N,0)

