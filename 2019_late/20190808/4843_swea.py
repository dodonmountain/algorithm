import sys
sys.stdin = open("input.txt")

T = int(input())

for t_case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    result = []
    # 평범한 버블 정렬 후 최댓값을 반환하는 함수 작성
    def bubble_pop(lst):
        for j in range(len(lst)):
            for i in range(len(lst)-1):
                if lst[i] <= lst[i+1]:
                    continue
                elif lst[i] > lst[i+1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
        return lst.pop(-1)
    # 평범한 버블 정렬 후 최솟값을 반환하는 함수 작성
    def bubble_popmin(lst):
        for j in range(len(lst)):
            for i in range(len(lst)-1):
                if lst[i] <= lst[i+1]:
                    continue
                elif lst[i] > lst[i+1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
        return lst.pop(0)
    # 10개를 출력해야 하므로 5번의 반복
    for i in range(5):
        result.append(bubble_pop(lst))
        result.append(bubble_popmin(lst))
    strs = ' '.join(map(str, result))
    print('#{} {}'.format(t_case+1, strs))