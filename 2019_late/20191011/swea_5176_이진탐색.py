import sys;sys.stdin=open('5176.txt')

def trav(arr, d):
    global res
    mid = len(arr) // 2
    left = arr[0:mid]
    right = arr[mid+1:N]
    if left:
        res.append((left[len(left) // 2],d + 1))
        if right:
            res.append((right[len(right) // 2],d + 1))
        if left:
            trav(left, d + 1)
            if right:
                trav(right, d + 1)
    

for t_case in range(int(input())):
    N = int(input())
    numbers = [i for i in range(1, N+1)]
    res = []
    res.append((numbers[len(numbers) // 2], 0))
    trav(numbers, 0)
    res.sort(key =lambda x:x[1])
    print('#{} {} {}'.format(t_case+1, res[0][0], res[(N>>1)-1][0]))