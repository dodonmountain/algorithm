def bubble_sort(arr):
    n= len(arr)
    for j in range(n):
        for i in range(0, n-1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr
for tc in range(10):
    a=int(input())
    b=list(map(int, input().split()))
    for i in range(a):
        bubble_sort(b)
        b[0] += 1
        b[-1] -= 1
    bubble_sort(b)
    print('#{} {}'.format(tc+1,b[-1] - b[0]))