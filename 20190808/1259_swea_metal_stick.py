import sys
sys.stdin = open("input.txt")

T = int(input())
for t_case in range(T):
    n = int(input())
    sticks = list(map(int, input().split())) #임시용 리스트
    nasa = [] # 2차원 배열 나사 세트
    base = [] # nasa[0]으로 시작해서 결과값까지 조립해나가는 첫 시작
    for i in range(0,  n*2, 2):
        nasa.append([sticks[i], sticks[i+1]])
    base.append(nasa.pop(0))
    # 탐색용 인덱스 초기화
    idx = 0
    while nasa: # nasa가 빈 리스트가 아니면
        if idx == len(nasa): # 검색자의 인덱스 값이 끝에 도달하면 다시 처음으로 돌아간다.
            idx = 0
        elif nasa[idx][0] == base[-1][-1]: # 순회하면서 숫나사와 암나사의 결합가능 여부를 확인한다.
            base.append(nasa.pop(idx))
        elif nasa[idx][1] == base[0][0]:
            base.insert(0, nasa.pop(idx))
        else:
            idx += 1 # 결합하지 않으면 검색자를 다음 위치로 이동

    res = []
    # 결과 값을 다시 문자열로 분리한다.
    for k in base:
        for j in k:
            res.append(j)

    result = ' '.join(map(str, res))
    print("#{} {}".format(t_case+1, result))


