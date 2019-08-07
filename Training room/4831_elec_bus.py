T = int(input())
for t_case in range(1, T+1):
    K, N, M = map(int, input().split())
    M_lst = list(map(int, input().split()))
    cnt = 0
    fuel = K
    ditance = 0
    M_lst.sort()
    # 정류장을 순회하면서 체크
    for i in range(0, len(M_lst)):
        distance = (M_lst[i] - M_lst[i-1]) if i != 0 else M_lst[i]
        fuel -= distance
        # 킹료조건
        if M_lst[i] + K >= N and fuel > -1:
            print('#{} {}'.format(t_case, cnt+1))
            break
        elif fuel > 0:
            # 다음정류장까지 갈수 있는지 체크
            # 갈수 있다면
            if fuel - (M_lst[i+1]-M_lst[i]) >= 0:
                continue
                # 여기는 패스
            else:
                # 갈 수 없다면 여기서라도 충전하자
                fuel = K
                cnt += 1
        # 만약 현재 정류장에서 연료가 바닥난다면
        elif fuel == 0:
            # 주유를 하자
            fuel = K
            cnt += 1
        # 둘다 아니면 파산!
        elif fuel < 0:
            print('#{} {}'.format(t_case, 0))
            break
        continue
