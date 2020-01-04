arr = [1,2,1,3,2,4,3,5,3,6,4,7,5,8,5,9,6,10,6,11,7,12,11,13]

V, E = 13, 12
L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)

def preorder(v):
    if v == 0: return
    print(v, end=' ')
    preorder(L[v])
    preorder(R[v])

def inorder(v):
    if v == 0: return
    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])

def postorder(v):
    if v == 0: return
    postorder(L[v])
    postorder(R[v])
    print(v, end=' ')

def treeHeight(v, height):
    global mxh
    if v == 0:
        if height > mxh:
            mxh = height
        return
    treeHeight(L[v], height+1)
    treeHeight(R[v], height+1)
    
def threeHeight(v, height):
    if v == 0:return
    if height == 3:
        print(v,end=' ')
        return
    threeHeight(L[v], height+1)
    threeHeight(R[v], height+1)

def treeSize(v):
    global t_size
    if v == 0:return
    t_size += 1
    treeSize(L[v])
    treeSize(R[v])
    
def anscestor(v):
    if P[v] == 1:
        ans.append(1)
        return
    ans.append(P[v])
    anscestor(P[v])

def LCA(a, b):
    if P[a] == P[b]:
        print('최소 공통 조상:', P[a])
        return
    if a > b:
        LCA(P[a], b)
    else:
        LCA(P[b], a)

for i in range(E*2):
    if not i & 1:
        if L[arr[i]]:
            R[arr[i]] = arr[i+1]
        else:
            L[arr[i]] = arr[i+1]
        P[arr[i+1]] = arr[i]

print('#1. 순회')
preorder(1)
print()
inorder(1)
print()
postorder(1)
print();print()
print('#2. 트리의 높이, treeHeight(v): v를 루트로 하는 트리의 높이 계산')
mxh = 0
treeHeight(1,0)
print(mxh)
print()
print('#3. 높이가 3인 노드들을 찾아서 출력하시오.')
threeHeight(1,0)
print()
print()
print('#4. 트리의 노드 수. treeSize(v): v를 루트로 하는 트리의 노드수 계산')
t_size = 0
treeSize(1)
print(t_size)
print()
print('#5. 9번 노드의 조상을 찾고, 13번 노드의 조상 찾고, 두 노드의 공통 조상')
ans = []
anscestor(9)
print(ans)
ans = []
anscestor(13)
print(ans)
LCA(9, 13)