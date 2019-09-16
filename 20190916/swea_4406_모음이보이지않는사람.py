import sys
sys.stdin = open('4406.txt')

T = int(input())

for t_case in range(T):
    word,res = list(input()),''
    for i in word:
        if i not in 'aeiou':
            res += i
    print('#{} {}'.format(t_case+1, res))