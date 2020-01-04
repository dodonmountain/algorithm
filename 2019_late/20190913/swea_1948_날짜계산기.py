import sys
sys.stdin = open('1948.txt')

T = int(input())
for t_case in range(T):
    m1, d1, m2, d2  = map(int, input().split())
    ds =[31,28,31,30,31,30,31,31,30,31,30,31]
    res = (sum(ds[:m2-1]) + d2) - (sum(ds[:m1-1]) + d1)
    print("#{} {}".format(t_case+1 , res + 1))