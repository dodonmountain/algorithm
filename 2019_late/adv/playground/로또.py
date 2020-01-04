import random
n = sorted(list(map(int, input().split())))
cnt = 0
while True:
    a = sorted(list(random.sample(range(1, 45), 6)))
    cnt += 1
    if a == n:
        print('당첨!!!!!')
        print('{}번 구매하였습니다. 총 구매비용:: {} 원'.format(cnt, cnt*1000))
        break

    
    
