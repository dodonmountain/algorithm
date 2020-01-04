import sys
sys.stdin = open('input.txt')

tries = int(input())
for test in range(1, tries + 1):
   stu_num = int(input())
   total_list = []
   for i in range(stu_num):
       a, b = map(int, input().split())
       one_tuple = tuple((b, a)) if a > b else tuple((a, b))
       if i == 0:
           total_list.append([one_tuple])
       else:
           for one_list in total_list:
               for one_t in one_list:
                   x = -1 if one_t[0] % 2 == 0 else 0
                   y = 1 if one_t[1] % 2 == 1 else 0
                   if (one_tuple[0] < one_t[0] + x and one_tuple[1] < one_t[0] + x) or \
                           (one_tuple[0] > one_t[1] + y and one_tuple[1] > one_t[1] + y):
                       flag = True
                   else:
                       flag = False
                       break
               if flag:
                   one_list.append(one_tuple)
                   break
           if not flag:
               total_list.append([one_tuple])
   print('#{} {}'.format(test, len(total_list)))