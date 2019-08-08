import sys
sys.stdin = open("input.txt")

T = int(input())


for t_case in range(T):
    P, A, B = map(int, input().split())
    left = 0
    right = P - 1
    book = list(range(1, P+1))
    # 이진탐색 A
    cntA = 0
    while left <= right:
        mid = (left+right) // 2 # 중앙값 설정
        if book[mid] == A: # 탐색 성공시 브레이크
            break
        elif book[mid] > A: # 중앙값이 목표값보다 클 경우 ( 목표가 왼쪽에 있을 경우)
            right = mid
            cntA += 1  # 반복마다 카운트
        else: # 중앙값이 목표값보다 작을 경우 ( 목표가 오른쪽에 있을 경우)
            left = mid
            cntA += 1  # 반복마다 카운트
    # 한번 더 이진탐색 초기화
    left = 0
    right = P - 1
    book = list(range(1, P+1))
    # 이진탐색 B
    cntB = 0
    while left <= right:
        mid = (left + right) // 2  # 중앙값 설정
        if book[mid] == B:  # 탐색 성공시 브레이크
            break
        elif book[mid] > B:  # 중앙값이 목표값보다 클 경우 ( 목표가 왼쪽에 있을 경우)
            right = mid
            cntB += 1  # 반복마다 카운트
        else:  # 중앙값이 목표값보다 작을 경우 ( 목표가 오른쪽에 있을 경우)
            left = mid
            cntB += 1  # 반복마다 카운트


    if cntA > cntB:
        print('#{} B'.format(t_case+1))
    elif cntB > cntA:
        print('#{} A'.format(t_case+1))
    else:
        print('#{} 0'.format(t_case+1))

