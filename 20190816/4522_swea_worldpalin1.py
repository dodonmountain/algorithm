import sys
sys.stdin = open('input.txt')

T = int(input())
for t_case in range(T):
    word = input()
    check = 'Exist'
    if '*' not in word and word != word[::-1]:
        check = 'Not exist'
    elif '*' not in word and word == word[::-1]:
        check = 'Exist'
    else:
        for i in range(len(word) // 2):
            if word[0] == '*':
                break
            elif word[-1] == '*':
                break
            elif word[i] != word[::-1][i]:
                if word[i] == '*' or word[::-1][i] == '*':
                    break
                else:
                    check = 'Not exist'
                    break
    print('#{} {}'.format(t_case + 1, check))

