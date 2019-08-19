import sys
sys.stdin = open('input.txt')

lst = list(map(int, input().split(', ')))
lst = [x for x in lst if x % 2]
print(', '.join(map(str, lst)))