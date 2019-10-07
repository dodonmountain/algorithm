import sys
sys.stdin = open('input.txt')
T = int(input())
for t_case in range(T):
    N, K = map(int, input().split())
    arr = []
    gpa = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
    for i in range(N):
        arr.append(list(map(int, input().split())))
    arr2 = {x:0 for x in range(1,N+1)}
    for j in range(N):
        total = arr[j][0]*35+arr[j][1]*45+arr[j][2]*20
        arr2[j+1] = total
    res = list(sorted(arr2.items(), key= lambda arr2: arr2[1], reverse=True))
    for i in range(N):
        if res[i][0] == K:
            rank = i + 1
            break
    for i in range(1,11):
        if rank <= (N//10)*i:
            print('#{} {}'.format(t_case+1, gpa[i-1]))
            break