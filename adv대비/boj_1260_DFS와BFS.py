import sys
sys.stdin = open('1260.txt')

V, E, S = map(int,input().split())
graph = []
for _ in range(E):
    graph.append(list(map(int, input().split())))

print(graph)