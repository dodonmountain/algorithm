import sys
sys.stdin = open('5986.txt')
import time
timing = time.time()

table = []
for i in range(2, 1000):
    flag = True
    for j in range(2, i):
        if not i % j:
            flag = False
    if flag:
        table.append(i)

def solve(s,d,ss,k):
    global cnt
    if k > N:
        return
    if d == 3:
        if k == N:
            cnt += 1
            return
        else:
            return
    for i in range(ss, end):
        s.append(table[i])
        solve(s,d+1,i,k+table[i])
        s.pop()

T = int(input())

for t_case in range(T):
    N = int(input())
    cnt = 0
    used = [0] * 168
    end = 168
    for i in range(168):
        if table[i] > N:
            end = i
            break
    solve([],0,0,0)
    print('#{} {}'.format(t_case+1, cnt))
print("time :", time.time() - timing)