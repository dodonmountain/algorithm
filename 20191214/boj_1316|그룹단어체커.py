T = int(input())
for tc in range(1, T+1):
    flag = False
    checker = [0] * 26
    word = input()
    cursor = word[0]
    checker[ord(word[0])-97] = 1
    for i in range(len(word)):
        if cursor == word[i]:continue
        else:
            if not checker[ord(word[i])-97]:
                checker[ord(word[i])-97] = 1
                cursor = word[i]
            else:
                flag = True
                break
    if flag:
        T -= 1
print(T)

