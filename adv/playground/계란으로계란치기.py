
def solve(s,d, cnt):
    global answer
    if cnt == 0:
        answer = N
        return
    if d == N or cnt < 2:
        answer = max(N - cnt, answer)
        return
    for i in range(N):
        if i == d:continue
        if s[i][0] > 0 and s[d][0] > 0:
            iw = s[i][1]
            dw = s[d][1]
            tmp = 0
            s[d][0] -= iw
            s[i][0] -= dw
            if s[d][0] < 1:
                tmp -= 1
            if s[i][0] < 1:
                tmp -= 1
            cnt -= tmp
            solve(s, d+1, cnt)
            s[d][0] += iw
            s[i][0] += dw
            cnt += tmp


from collections import deque

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]
answer = -1
solve(eggs, 0, N)
print(answer)