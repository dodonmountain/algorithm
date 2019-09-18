import sys
sys.stdin = open('4676.txt')

T = int(input())

for t_case in range(T):
    word = list(input())
    L = len(word)
    H = int(input())
    arr = sorted(list(map(int, input().split())),reverse=True)
    for k in arr:
        word.insert(k, '-')
    res = ''.join(word)
    print('#{} {}'.format(t_case+1, res))
