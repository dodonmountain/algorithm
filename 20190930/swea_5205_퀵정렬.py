import sys; sys.stdin = open('5205.txt')

# from random import randint
# def quick_sort(arr):
# 	if len(arr) > 1:
# 		pivot = arr[randint(0, len(arr)-1)]
# 		r, l = [i for i in arr if i > pivot], [i for i in arr if i < pivot]
# 		mid = [i for i in arr if i == pivot]
# 		return quick_sort(l) + mid + quick_sort(r)
# 	return arr

def _partition(arr, lo, hi):
    pivot = arr[hi]
    i = lo - 1
    for j in range(lo, hi):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[hi], arr[i + 1] = arr[i + 1], arr[hi]
    return i + 1

def _quicksort(arr, lo, hi):
    if lo < hi:
        p = _partition(arr, lo, hi)
        _quicksort(arr, lo, p - 1)
        _quicksort(arr, p + 1, hi)
    return arr

def quick_sort(arr):
    return _quicksort(arr, 0, len(arr) - 1)

for t_case in range(int(input())):
    N = int(input())
    arr = list(map(int, input().split()))
    flag = False
    for i in range(N - 1, -1, -1):
        if arr[i] < arr[i-1]:
            flag = True
            break
    if flag:
        arr = quick_sort(arr)
    print('#{} {}'.format(t_case+1, arr[(N-1>>1)+1]))
