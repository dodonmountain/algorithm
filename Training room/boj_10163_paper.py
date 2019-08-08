import sys
sys.stdin = open("input.txt")

N = int(input())
a = [[0]*101 for _ in range(101)]

def count(array, t):
    result = 0
    for k in range(101):
        for l in range(101):
            if array[k][l] == t:
                result += 1
    return result

for t_case in range(N):
    lst = list(map(int, input().split()))
    for j in range(lst[3]):
        for i in range(lst[2]):
            a[lst[0]+i][lst[1]+j] = t_case+1
for i in range(N):
    print(count(a,i+1))








