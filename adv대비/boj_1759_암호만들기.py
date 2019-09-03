import sys
sys.stdin = open('1759.txt')
from itertools import permutations as pm
L, C = map(int, input().split())
pword = list(input().split())
tmp = []
