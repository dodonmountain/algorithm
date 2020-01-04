import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
   word = input()
   res = 0
   for i in range(len(word)):
       if word[i] != word[-i-1]:
           if word[i] == '?' or word[-i-1] == '?':
               if i == len(word) // 2:
                   res = 1
                   break
               continue
           else:
               break
       else:
           res = 1
   if res:
       print('#{} Exist'. format(tc))
   else:
       print('#{} Not exist'. format(tc))