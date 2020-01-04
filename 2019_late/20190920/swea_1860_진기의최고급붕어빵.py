import sys
sys.stdin = open('1860.txt')

T = int(input())

for t_case in range(T):
    n,m,k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    timeline = [0] * (max(arr) + 1)
    for i in arr:
        timeline[i] = arr.count(i)
    hp = 0
    flag = True
    for i in range(len(timeline)):
        if i > 0:
            if i % m == 0:
                hp += k
        if timeline[i]:
            hp -= timeline[i]
            if hp < 0:
                flag = False
                break
    if flag:
        res = 'Possible'
    else:
        res = 'Impossible'
    print('#{} {}'.format(t_case+1, res))