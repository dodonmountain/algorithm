# 190824 TIL

## 알고리즘

### 백준 #2231 분해합

1. 코드

```python
# https://www.acmicpc.net/problem/2231

N = int(input())

def bh(num):
    original = num
    tmp = []
    if num < 10:
        return -1
    else:
        while num:     
            tmp.append(num % 10)
            num = num // 10
        return num + sum(tmp) + original
# main   
for i in range(N + 1):
    if i == N:
        print(0)
    elif bh(i) == N:
        print(i)
        break
```

2. 설명

   문제의 개요는 분해합이 N이 되는 생성자의 최솟값을 출력하는 것이다.

   내 코드의 구성은 아래와 같다.

	* 함수 bh는 분해합이 존재할 경우 분해합을 출력한다. 
	* main 부분에서는 0부터 N + 1까지 분해합을 수행하며 분해합의 결과가 N이면 i를 출력하고 break
	* N까지 검색해도 못 찾았을 경우 0을 출력한다.

3. Point
   * 없다. 풀이 과정이 단순하고 직관적인 문제이다.



### SWEA 4874 Forth

1. 코드

   ```python
   T = int(input())
   
   for t_case in range(T):
       ipt = list(input().split())
       stack = []
       for i in ipt:
           if i == '.':
               if len(stack) > 1:
                   res = 'error'
               else:
                   res = stack.pop()
                   break
           elif i not in '+-*/':
               stack.append(i)
           elif len(stack) < 2:
               res = 'error'
               break
           else:
               if i == '+':
                   b = int(stack.pop())
                   a = int(stack.pop())
                   stack.append(a+b)
               elif i == '-':
                   b = int(stack.pop())
                   a = int(stack.pop())
                   stack.append(a-b)
               elif i == '*':
                   b = int(stack.pop())
                   a = int(stack.pop())                
                   stack.append(a*b)
               elif i == '/':
                   b = int(stack.pop())
                   a = int(stack.pop())                
                   stack.append(a//b)
               else:
                   res = 'error'
                   break
       print('#{} {}'.format(t_case+1, res))
   ```

   

2. 설명

   * 예외처리를 하나씩 하다 보니 무식한 코드가 되었다.
   * postfix로 표기된 계산식의 결과를 출력하는 코드이다.
   * 숫자일 경우 숫자를 받아서 스택에 저장 -> `+-*/` 일 경우 해당 연산을 수행후 스택에 돌려 놓기 -> `.` 일 경우 연산종료 후 출력하면 된다.
   * 오류가 발생할경우 error를 출력한다.

3. Point

   * 처음에 오류가 연산자의 수가 더 많은 IndexError만 있다고 생각해서 `try ~ except`로 처리하려 했지만 당연히 실패한다.
   * 다종다양한 엣지케이스에 대응하기 위해 모든 조건을 매우 한정적으로 바꾸었다.
   * 연산자를 좀 더 유려하게 저장할 수 있을것 같다.

### SWEA 4875 미로찾기

> 부등호 방향을 주의하자 언제나

1. 코드

   ```python
   T = int(input())
   
   for t_case in range(T):
       N = int(input())
       maze = []
       for _ in range(N):
           maze.append(list(map(int, list(input()))))
       for i in range(N):
           for j in range(N):
               if maze[i][j] == 2:
                   start = [i, j]
               elif maze[i][j] == 3:
                   goal = (i, j)
                   maze[i][j] = 0
       stack = [start]
       i, j = start[0], start[1]
       visited = [[0] * N for _ in range(N)]
       res = 0
       while stack:
           i,j = stack.pop()
           if i == goal[0] and j == goal[1]:
               res = 1
               visited[i][j] = 9
               break
           visited[i][j] = 1
           if i > 0:
               if maze[i - 1][j] == 0 and visited[i-1][j] ==0: # up
                   stack.append((i - 1, j))
           if i < N - 1:
               if maze[i + 1][j] == 0 and visited[i+1][j] ==0: # down 
                   stack.append((i + 1, j))
           if j < N - 1:
               if maze[i][j + 1] == 0 and visited[i][j+1] ==0: # right
                   stack.append((i, j + 1))
           if j > 0:
               if maze[i][j - 1] == 0 and visited[i][j-1] ==0: # left
                   stack.append((i, j - 1))
       print("#{} {}".format(t_case+1, res))
   ```

   

2. 설명

   * 2에서 출발해서 3으로 가는 미로찾기. 벽은 1 통로는 0으로 표현
   * 역시나 허접답게 모든 경우의 수를 if문으로 분기한 슬픈 광경을 볼 수 있다.
   * `+`와 `-`  그리고 `<`와 `>`를 헷갈려서 쓸데없이 시간을 소비했다.
   * 엣지케이스를 찾으려고 했지만 오타를 찾게 되었다.
   * 오타가 나도 샘플케이스를 통과하는 경우는 너무너무 슬픈것같다.

3. 포인트

   * `visited`를 2차원 리스트로 선언하는데 익숙해졌다.
   * 이게 DFS인지 BFS인지 헷갈린다. 공부가 더 필요하다.