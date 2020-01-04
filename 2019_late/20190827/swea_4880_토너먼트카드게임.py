import sys
sys.stdin = open("input.txt")

T = int(input())

def game(a, b): # 가위바위보, 낸 손 모양이 아니라 인덱스를 리턴해야함
    A, B = lst[a-1], lst[b-1]
    vs = {1: 3, 2: 1, 3: 2}    
    if vs[A] == B:
        return a
    if vs[B] == A:
        return b
    return a

def divide(start, end):
    if start == end: # 종료 조건. 시작과 끝이 같으면 나눌수 없다 => 우승자 결정
        return start
    left, right = divide(start, (start + end) //2), divide((start + end) // 2 + 1, end) # start + end 를 괄호로 감싸는것은 중요했다.
    return game(left, right)

for t_case in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    print("#{} {}".format(t_case+1, divide(1, N)))

