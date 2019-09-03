import sys
sys.stdin = open('1759.txt')
from itertools import combinations as cb
L, C = map(int, input().split())
pword = sorted(input().split())
#print(L,C, pword)
for word in cb(pword, L):
    res, vowel, jaum ='', 0, 0
    for i in range(len(word)):
        if word[i] in "aeiou":
            vowel += 1
        else:
            jaum = jaum + 1
        res += word[i]
    if vowel > 0 and jaum > 1:
        print(res)
