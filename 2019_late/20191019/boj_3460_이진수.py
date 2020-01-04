for tc in range(int(input())):
    n = int(input())
    arr = bin(n).lstrip('0b')[::-1]
    for i in range(len(arr)):
        if arr[i] == '1':
            print(i, end=' ')
