import sys
sys.stdin = open('1987.txt')
input = sys.stdin.readline

def solve(here,depth):
    global MAX
    if MAX == 25:
        return
    if depth > MAX:
        MAX = depth
    x,y = here[0], here[1]
    if 0<= x+1 < r  and  0 <= y < c:
        if not used[board[x+1][y]]:
            used[board[x+1][y]] = 1
            solve((x+1,y),depth + 1)
            used[board[x+1][y]] = 0
    if 0<= x < r  and  0 <= y+1 < c:
        if not used[board[x][y+1]]:
            used[board[x][y+1]] = 1
            solve((x,y+1),depth + 1)
            used[board[x][y+1]] = 0
    if 0<= x-1 < r  and  0 <= y < c:
        if not used[board[x-1][y]]:
            used[board[x-1][y]] = 1
            solve((x-1,y),depth + 1)
            used[board[x-1][y]] = 0
    if 0<= x < r  and  0 <= y-1 < c:
        if not used[board[x][y-1]]:
            used[board[x][y-1]] = 1
            solve((x,y-1),depth + 1)
            used[board[x][y-1]] = 0

r, c = map(int, input().split())
board = [list(map(lambda x:ord(x)-64,input())) for _ in range(r)]
used = [0]*27
dx,dy = [1,0,-1,0], [0,1,0,-1]
MAX = -1
used[board[0][0]] = 1
solve((0,0),0)
print(MAX+1)