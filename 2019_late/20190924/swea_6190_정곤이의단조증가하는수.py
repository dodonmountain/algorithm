import sys
sys.stdin = open('6190.txt')

def danjo(num):
    while num:
        b = num % 10
        num //= 10
        a = num % 10
        if a > b:
            return False
    return True

def solve(s):
    tmp = -1
    for j in range(N):
        for i in range(N):
            if i < j:
                if danjo(arr[i] * arr[j]):
                    if tmp < arr[i] * arr[j]:
                        tmp = arr[i] * arr[j]
    return tmp

for t_case in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse=True)
    print('#{} {}'.format(t_case+1, solve(0)))
