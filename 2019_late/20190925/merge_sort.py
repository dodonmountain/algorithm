# 병합정렬 > 연결리스트에 적합
# python List app,pop,slice 사용시 시간 문제
arr = [69, 10, 30, 2, 16, 8 ,31, 22]
tmp = [0] * len(arr)

def mergeSort(low, hi):
    if low == hi:return

    mid = (low + hi) >> 1
    mergeSort(low, mid)
    mergeSort(mid + 1, hi)
    # 왼쪽과 오른쪽이 정렬된 상태
    i, j, k = low, mid + 1, low
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]; k, i = k + 1, i + 1
        else:
            tmp[k] = arr[j]; k, j = k + 1, j + 1
    while i <= mid:
        tmp[k] = arr[i]; k, i = k + 1, i + 1
    while j <= hi:
        tmp[k] = arr[j]; k, j = k + 1, j + 1
    
    for x in range(low, hi + 1):
        arr[x] = tmp[x]
print(arr)
mergeSort(0, len(arr)-1)
print(arr)