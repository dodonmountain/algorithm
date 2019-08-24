import sys
sys.stdin = open("input.txt")

T = int(input())
def game(lst):
    a, b = lst[0], lst[1]
    vs = {
        1: 3,
        2: 1,
        3: 2,
    }    
    if vs[a] == b:
        return a
    elif vs[b] == a:
        return b
    elif a == b:
        return a

def divide(lst):
    if len(lst) > 1:
        left = lst[:len(lst)//2] if len(lst) % 2 == 0 else lst[:(len(lst)//2)+1]
        right= lst[len(lst)//2:] if len(lst) % 2 == 0 else lst[(len(lst)//2)+1:]
        return [divide(left),divide(right)]
    else:
        return lst[0]
        
for t_case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    print(game(divide(lst)))

