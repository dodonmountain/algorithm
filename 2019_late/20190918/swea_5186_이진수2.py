import sys
sys.stdin = open('5186.txt')

T = int(input())

for t_case in range(T):
    N = input()
    N = float(N)
    arr = []
    for i in range(1,13):
        arr.append(2**-i)
    stack,res = [],[]
    i = 0
    flag = False
    while i < 13:
        if i == 12:
            flag = True
            break
        if sum(stack) == N:
            break
        else:
            if sum(stack) + arr[i] > N:
                i += 1
                continue
            else:
                stack.append(arr[i])
                res.append(i)
    if flag:
        print('#{} overflow'.format(t_case+1))
    else:
        result = [0] * 12
        for i in res:
            result[i] = 1
        ff = ''.join(list(map(str, result))).rstrip('0')
        print('#{} {}'.format(t_case+1, ff))

    
        
    
