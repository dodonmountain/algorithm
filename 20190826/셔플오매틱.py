import sys
sys.stdin = open('ttinput.txt')


T = int(input())
def s_o_matic(left, right, x):
    long = left + right
    if x == 0:
        return(left + right)
    else:
        for i in range(x):
            long[len(left)-i-1:len(left)-i], long[len(left)+i:len(left)+i+1] = long[len(left)+i:len(left)+i+1], long[len(left)-i-1:len(left)-i]
        return long





for t_case in range(T):
    N = int(input())
    cards = list(map(int, input().split()))
    left = cards[:len(cards)//2]
    right = cards[len(cards)//2 +1:]
    print(s_o_matic(left, right, 0))