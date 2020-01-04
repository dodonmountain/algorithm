import sys
sys.stdin = open('5203.txt')

def check_triplet(lst):
    for i in range(10):
        if lst.count(i) >= 3:
            return True
    return False

def check_run(lst):
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            for k in range(j,len(lst)):
                if lst[k] - lst[j] == 1 and lst[j] - lst[i] == 1:
                    return True 
    return False

for t_case in range(int(input())):
    arr = list(map(int,input().split()))
    arr, win = arr[::-1], 0
    p1_hand, p2_hand = [], []
    while arr:
        p1_hand.append(arr.pop())
        p1_hand.sort()
        if check_triplet(p1_hand) or check_run(p1_hand):
            win = 1
            break
        p2_hand.append(arr.pop())
        p2_hand.sort()
        if check_triplet(p2_hand) or check_run(p2_hand):
            win = 2
            break
    print('#{} {}'.format(t_case+1, win))
        