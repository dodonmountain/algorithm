import sys
sys.stdin = open('1221.txt')

for t_case in range(int(input())):
    q, n = input().split();n = int(n)
    arr = list(input().split())
    cod = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    arr.sort(key= lambda arr : cod.index(arr))
    print(q, *arr)