import sys
sys.stdin = open("input.txt")
from collections import deque
T = int(input())

for t_case in range(T):
    words = input()
    stack = deque(words)
    tmp = deque()
    print(stack)
    here = stack.popleft()
    while True:
        

        