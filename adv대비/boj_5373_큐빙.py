import sys
sys.stdin = open('5373.txt')
from pprint import pprint
T = int(input())
for t_case in range(T):
    n = int(input())
    task = []
    task.append(list(input().split()))
    #윗면 = 흰색
    U = [['w']*3 for _ in range(3)]
    # 아랫면 = 노란색
    D = [['y']*3 for _ in range(3)]
    # 앞면 = 빨간색
    F = [['r'] * 3 for _ in range(3)]
    # 뒷면 = 오렌지색
    B = [['o'] * 3 for _ in range(3)]
    # 왼쪽면 = 초록색
    L = [['g'] * 3 for _ in range(3)]
    # 오른쪽 면 = 파란색
    R = [['b'] * 3 for _ in range(3)]
    Z = [['-']*3 for _ in range(3)]
    cube = [[Z, U, Z, Z],
            [L, B, R, F],
            [Z, D, Z, Z]]
    for j in range(len(task)):
        for k in range(len(task)):
            print(task[j])