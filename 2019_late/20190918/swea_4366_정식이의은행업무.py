import sys
sys.stdin = open('4366.txt')

T = int(input())

for t_case in range(T):
    b = list(map(int, list(input())))
    t = list(map(int, list(input())))
    comp = []
    for i in range(len(b)-1,-1,-1):
        if b[i] == 0:
            b[i] = 1
            res = 0
            k = 0
            for j in range(len(b)-1,-1,-1):
                res += b[j] * (2 ** k)
                k += 1
            comp.append(res)
            b[i] = 0
        else:
            b[i] = 0
            res = 0
            k = 0
            for j in range(len(b)-1,-1,-1):
                res += b[j] * (2 ** k)
                k += 1
            comp.append(res)
            b[i] = 1      
    comp2 = []
    for i in range(len(t)-1,-1,-1):
        if t[i] == 0:
            for l in range(1,3):
                t[i] = l
                res = 0
                k = 0
                for j in range(len(t)-1,-1,-1):
                    res += t[j]  * (3 ** k)
                    k += 1
                comp2.append(res)
            t[i] = 0
        elif t[i] == 1:
            for l in range(0,3,2):
                t[i] = l
                res = 0
                k = 0
                for j in range(len(t)-1,-1,-1):
                    res += t[j]  * (3 ** k)
                    k += 1
                comp2.append(res)
            t[i] = 1
        else:            
            for l in range(2):
                t[i] = l
                res = 0
                k = 0
                for j in range(len(t)-1,-1,-1):
                    res += t[j]  * (3 ** k)
                    k += 1
                comp2.append(res)
            t[i] = 2
    for i in comp:
        if i in comp2:
            res = i
            break
    print('#{} {}'.format(t_case+1, res))
