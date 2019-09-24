import sys
sys.stdin = open('7854.txt')
table = []
for i in range(1, 1000):
    if int('9145643523' + str(i)) % i == 0:
        table.append(i)
print(table)
# for t_case in range(int(input())):
#     X = int(input())
    
