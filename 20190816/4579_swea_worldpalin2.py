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
            # 대칭되는 원소가 서로 다르고 둘중 하나가 애스터리스크가 아닐 때
            if word[i] != word[::-1][i] and word[i] != '*' and word[::-1][i] != '*':
                check = 'Not exist'
                break
            elif word[i] == word[::-1][i]:
                continue
            else:
                check = 'Not exist'
    print('#{} {}'.format(t_case + 1, check))


