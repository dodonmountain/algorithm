import sys
sys.stdin = open("input.txt")
T = int(input())
numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t_case in range(T):
    counter = []
    result = ''
    cn, c_len = input().split()
    arr = list((input().split()))
    for n in numbers:
        counter.append(arr.count(n))
    for i in range(10):
        result += (numbers[i] + ' ') * counter[i]
    print('#{}'.format(t_case+1))
    print(result)