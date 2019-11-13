brd = [list(range(10)) for _ in range(10)]
W, H = 10, 10
for i in range(W):
    tmp = []
    for j in range(H):
        if brd[j][i]:
            tmp.append(brd[j][i])
    tmp = ([0] * (H - len(tmp))) + tmp
    for j in range(H):
        brd[j][i] = tmp[j]
        
            
