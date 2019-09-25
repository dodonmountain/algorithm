import sys; sys.stdin = open('1219.txt')

def dfs(s):
    global flag
    visit[s] = 1
    for w in G[s]:
        if w == 99:
            flag = True
            return
        if not visit[w]:
            dfs(w)

for t_case in range(10):
    t, E = map(int, input().split())
    arr = list(map(int, input().split()))
    G = [[]for _ in range(E)]
    for i in range(len(arr)):
        if not i & 1:
            G[arr[i]] += [arr[i+1]]
    visit = [0] * (E + 1); flag = False
    dfs(0)
    print('#{} {}'.format(t, int(flag)))
    