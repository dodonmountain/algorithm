N = 5
tmp = 0xffffffffffffff

def jump(s, k):
    global N, tmp
    if k > tmp and s > 0:
        return
    if s == N:
        if k < tmp and s > 0:
            tmp == k
        return
    elif s > N:
        return
    else:
        for i in range(s, N):
            jump(s+i,k+i)
print(jump(0,0))