import sys
sys.stdin = open('input.txt')

T = int(input())

for t_case in range(T):
    p,q,r,s,w = map(int, input().split())
    ra = p * w
    if w <= r:
        rb = q
    else:
        rb = (w - r) * s + q
    if ra < rb:
        res = ra
    else:
        res = rb
    print('#{} {}'.format(t_case+1, res))