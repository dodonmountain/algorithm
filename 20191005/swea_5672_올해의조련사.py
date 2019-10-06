import sys;sys.stdin=open('5672.txt')


def solve():
    l, r = 0, N - 1
    answer = ''
    while l < r:
        if arr[l] < arr[r]:
            answer += arr[l]
            l += 1
        elif arr[l] > arr[r]:
            answer += arr[r]
            r -= 1
        else:
            ll, rr = l + 1, r - 1
            while ll < rr:
                if arr[ll] == arr[rr]:
                    ll += 1
                    rr -= 1
                else:
                    break
            if arr[ll] < arr[rr]:
                answer += arr[l]
                l += 1
            else:
                answer += arr[r]
                r -= 1
    answer += arr[r]
    return answer
            
            
for t_case in range(int(input())):
    N = int(input())
    arr = [input().strip() for _ in range(N)]
    answer = solve()
    print('#{} {}'.format(t_case+1, answer))