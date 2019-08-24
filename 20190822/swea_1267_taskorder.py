import sys

sys.stdin = open("input.txt")
"""
    lines[2*i+1] =>  도착 노드 (홀수)
    lines[2*i] =>  출발 노드 (짝수)
    터미널 노드부터 간선을 지워나간다
    간선의 도착점에 위치한 노드는 터미널 노드가 아니고 시작점이 될 수 없다.
    => 시작점이 될 수 없는 노드를 리스트에 저장 => visited []
    => 시작점이 될 수 있는 노드라면
        => 방문 예정 리스트에 저장
            => 만약 방문 예정리스트중에 결과에 없는 노드가 있으면
                => 결과에 저장
    => 전체 간선 리스트에서 방문 예정 리스트의 간선 정보를 pop
    => 연결점이 없는 노드를 결과에 추가
"""
T = 3
for t_case in range(T):
    V, E = map(int, input().split())
    lines = list(map(int, input().split()))
    result = []
    #  도착 노드를 모두 방문 기록한다.
    while lines:
        visited = [-1] * (V + 1) # -1 미방문
        check = []
        for i in range(len(lines) // 2):
            visited[lines[2 * i + 1]] = 1  # 1 방문
        for j in range(1, len(visited)):
            if visited[j] == -1:
                check.append(j)
                if j not in result:
                    result.append(j)
        # 앞에서 부터 뽑으면 인덱스 에러 발생
        # 뒤에서 부터 순회하면서 뽑으면 안락
        check.sort()
        for k in range(len(lines)-1,-1,-1):
            if k % 2 == 0:
                if lines[k] in check:
                    lines.pop(k)
                    lines.pop(k)
    for l in range(1, V+1):
        if l not in result:
            result.append(l)
    print("#{} {}".format(t_case+1, ' '.join(map(str, result))))
