data = [69, 10, 30, 2, 16, 8, 31, 22]

# 힙 구현
H = [0] * 100   # 저장소
top = 0

def push(item):
    global top
    top += 1
    H[top] = item
    child, parent = top, top >> 1
    while parent:
        if H[child] < H[parent]:
            H[parent], H[child] = H[child], H[parent]
        child = parent
        parent = child // 2

def pop():
    global top
    # empty check 생략
    ret = H[1]
    H[1] = H[top]
    top -= 1
    parent, child = 1, 2
    while child <= top:
        if child + 1 <= top and H[child] > H[child + 1]:
            child += 1
        if H[child] < H[parent]:
            H[parent], H[child] = H[child], H[parent]
            child = parent * 2
            parent = child
        else: break
    return ret

for val in data:
    push(val)

while top:
    print(pop(), end=' ')