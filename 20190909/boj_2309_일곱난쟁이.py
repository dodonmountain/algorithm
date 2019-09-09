import sys
sys.stdin = open('2309.txt')

dwarves = []
# 난쟁이를 받을 배열 선언
for _ in range(9):
    dwarves.append(int(input()))
# 아홉 난쟁이의 리스트 완성
dwarves.sort()
# 일곱난쟁이의 키의 합은 100
# 함수로 풀어보자!
# 매개변수 s를 배열로 가지는 함수 seven 정의
def seven(s,n):
    # 종료 조건은 s의 합이 100이고, 총 7명일 때
    global flag
    if n == 7:
        if sum(s) == 100:
            for i in s:
                print(i)
            flag = False
            return
    if flag:
        for i in range(9):
            if not used[i]:
                used[i] = 1 # 중복체크
                s.append(dwarves[i])
                # 여기서 재귀
                seven(s,n + 1) # 한명씩 늘려나간다.
                s.pop()
                used[i] = 0
flag = True
used = [0] * 9
seven([],0)
# 근데 그냥 하면 모든 경우의 수가 나와버림
# flag 변수를 써보자
# 성공!