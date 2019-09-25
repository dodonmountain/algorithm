tmp = 50000
def solution(n):
    def solve(now, bt):
        global tmp
        if now == n:
            if bt < tmp:
                tmp = bt
            return
        if now*2 <= n and now != 0:
            solve(now*2, bt)
        else:
            if n - now < 5:
                for i in range(1, 6):
                    solve(now + i, bt + i)
            else:
                solve(now+1, bt+1)
                
    solve(1, 1)
    return tmp

print(solution(500))