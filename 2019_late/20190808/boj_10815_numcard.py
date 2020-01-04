import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt")

N = int(input())
n_lst = set(map(int, input().split()))
M = int(input())
m_lst = list(map(int, input().split()))
k_lst = []
for i in range(len(m_lst)):
    if m_lst[i] in n_lst:
        k_lst += [i]
result = [0] * len(m_lst)
for i in range(len(k_lst)):
    result[k_lst[i]] = 1

print(' '.join(map(str, result)))

