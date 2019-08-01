T = int(input())
for t_case in range(T):
R, S = input().split()
R = int(R)
result = ''
for i in list(S):
    result += i*3
print(result)