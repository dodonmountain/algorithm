import sys
sys.stdin = open("input.txt")

T = int(input())
# 초기화
A = list(range(1, 13))
n = len(A)
C = []
# 모든 부분집합 구하기
for i in range(1 << n):  # 1<<n == 2**n == 부분집합의 갯수
    B = []
    for j in range(n):  # 원소의 수만큼 비트를 비교
        if i & (1 << j):  # i의 j번째 비트가 1이면 j번째 원소를 B에 어펜드
            B.append(A[j])
    C.append(B)  # 하나의 비교연산이 끝나면 B를 C에 어펜드
# range(1,13)의 모든 부분집합을 내부 리스트로 갖는 2차원 리스트 C 저장
# 문제 시작
for t_case in range(T):
    N, K = map(int, input().split())
    cnt = 0
    for i in C:
        if len(i) == N:
            if sum(i) == K:
                cnt += 1
    print('#{} {}'.format(t_case+1, cnt))






