import sys;sys.stdin=open('1932.txt')

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
maxnow = tri[0][0]

for i in range(1, n):
    for j in range(len(tri[i])):
        if i == j:
            tri[i][j] = tri[i][j] + tri[i-1][j-1]
        else:
            if j-1 >= 0:
                tri[i][j] = max(tri[i][j] + tri[i-1][j], tri[i][j] + tri[i-1][j-1])
            else:
                tri[i][j] = tri[i][j] + tri[i-1][j]
print(max(tri[n-1]))