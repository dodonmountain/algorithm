V, E = 13, 12
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)
# tree = [[0,0,0] for _ in range(V+1)]
# tree = [[] for _ range(V+1)]

arr = [1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]

for i in range(E*2):
    if not i & 1:
        if L[arr[i]]:
            R[arr[i]] = arr[i+1]
        else:
            L[arr[i]] = arr[i+1]
        P[arr[i+1]] = arr[i]
# for i in range(13):
#     print(L[i], R[i])
# ---------------------
def inorder(v):
    if v == 0: return
    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])
# ---------------------
inorder(1)