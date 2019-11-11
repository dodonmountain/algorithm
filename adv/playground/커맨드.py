T = int(input())

for tc in range(T):
    arr = list(input())
    if arr[0] == arr[1] == arr[4]:
        if arr[2] == arr[3] == arr[5] ==arr[6]:
            if arr[0] != arr[2]:
                print(1)
                continue
    print(0)