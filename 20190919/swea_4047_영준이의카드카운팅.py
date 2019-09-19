import sys
sys.stdin = open('4047.txt')

T = int(input())
 
for t_case in range(T):
    dicts = {'S{}'.format(i): 0 for i in range(1, 14)}
    dictd = {'D{}'.format(i): 0 for i in range(1, 14)}
    dicth = {'H{}'.format(i): 0 for i in range(1, 14)}
    dictc = {'C{}'.format(i): 0 for i in range(1, 14)}
    cards = input()
    res = []
    for i in range(0, len(cards), 3):
        if cards[i] =='S':
            dicts[cards[i]+str(int(cards[i+1])*10 + int(cards[i+2]))] += 1
        elif cards[i] =='D':
            dictd[cards[i]+str(int(cards[i+1])*10 + int(cards[i+2]))] += 1
        elif cards[i] =='H':
            dicth[cards[i]+str(int(cards[i+1])*10 + int(cards[i+2]))] += 1
        elif cards[i] =='C':
            dictc[cards[i]+str(int(cards[i+1])*10 + int(cards[i+2]))] += 1
    cnt = 0
    for i in dicts.values():
        if i == 0:
            cnt += 1
        elif i >= 2:
            cnt = 'ERROR'
            break
    res.append(cnt)
    cnt = 0
    for i in dictd.values():
        if i == 0:
            cnt += 1
        elif i >= 2:
            cnt = 'ERROR'
            break
    res.append(cnt)
    cnt = 0
    for i in dicth.values():
        if i == 0:
            cnt += 1
        elif i >= 2:
            cnt = 'ERROR'
            break
    res.append(cnt)
    cnt = 0
    for i in dictc.values():
        if i == 0:
            cnt += 1
        elif i >= 2:
            cnt = 'ERROR'
            break
    res.append(cnt)
    cnt = 0
    if 'ERROR' in res:
        res = 'ERROR'
    else:
        res = ' '.join(map(str, res))
    print("#{} {}".format(t_case+1,res))