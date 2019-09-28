import sys; sys.sydin = open('5204.txt')

def mergeSort(low, hi):
    print('arr:',arr)
    print('tmp:',tmp)
    if low == hi: # 길이가 1인 경우
        return
    mid = (low + hi) >> 1
    mergeSort(low, mid)
    mergeSort(mid + 1, hi)
    # 왼쪽과 오른쪽이 정렬된 상태
    i, j, k = low, mid + 1, low
    while i <= mid and j <= hi:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            k += 1
            i += 1
        else:
            tmp[k] = arr[j]
            k += 1
            j += 1
    while i <= mid:
        tmp[k] = arr[i]
        k += 1
        i += 1
    while j <= hi:
        tmp[k] = arr[j]
        k += 1
        j += 1
    for x in range(low, hi + 1):
        arr[x] = tmp[x]
arr =[2,2,1,1,3]
tmp = [0] * len(arr)
print(arr)
mergeSort(0, len(arr)-1)
print(arr)