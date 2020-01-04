dic = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for i in dic:
    print(i)
    word = word.replace(i, 'A')
print(len(word))