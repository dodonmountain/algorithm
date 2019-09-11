import sys
sys.stdin = open('1945.txt')
T = int(input())
for t_case in range(T):
    N = int(input())
    flag = True
    for a in range(24):
        if not flag:
            break
        for b in range(23):
            if not flag:
                break
            for c in range(22):
                if not flag:
                    break
                for d in range(21):
                    if not flag:
                        break
                    for e in range(20):
                        if (2**a) * (3**b) * (5**c) * (7**d) * (11**e) == N:
                            print("#{} {} {} {} {} {}".format(t_case+1, a,b,c,d,e))
                            flag = False
                            break