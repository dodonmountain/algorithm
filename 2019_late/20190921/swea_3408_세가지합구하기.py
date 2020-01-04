import sys
sys.stdin = open('3408.txt')

T = int(input())

for t_case in range(T):
    N = int(input())
    s1 = (1 + N) * (N//2)
    s2 = (1 + (2*N)-1) * (N // 2)
    s3 = (2 + 2*N) * (N // 2)
    if N & 1:
        s1 += 1 + N//2
        s2 += (2*N)//2
        s3 += 1 + (2*N)//2
    print('#{}'.format(t_case+1),s1,s2,s3)