def q_Sort(lo,hi):
    if lo>=hi:
        return
    i, j = lo, hi
    while i < j:
        while arr[lo] > arr[i]:
            i += 1
        while arr[lo] < arr[j]:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[lo], arr[j] = arr[j], arr[lo]
    q_Sort(lo, j - 1)
    q_Sort(j + 1, hi)

N = int(input())
arr = [int(input()) for x in range(N)]
q_Sort(0, N-1)
for i in arr:
    print(i)