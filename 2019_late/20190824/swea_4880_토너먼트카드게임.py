import sys
sys.stdin = open("input.txt")

T = int(input())

def game(lst):
    if len(lst) < 2:
        return lst[0]
    else:
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
    if len(lst) > 2:
        left = lst[:len(lst)//2] if len(lst) % 2 == 0 else lst[:(len(lst)//2)+1]
        right= lst[len(lst)//2:] if len(lst) % 2 == 0 else lst[(len(lst)//2)+1:]
        return left
    else:
        return lst
        

for t_case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    check = [0 for x in range(len(lst))]
    print(divide(lst))
    print(lst)
    