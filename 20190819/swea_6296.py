import sys
sys.stdin = open('input.txt')

words = list(input().split(', '))

print(', '.join(sorted(words, key=str.lower)))