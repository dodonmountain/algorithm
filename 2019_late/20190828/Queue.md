# Queue

* 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
* 선입선출구조(FIFO: First In First Out)
  * 큐에 삽입한 순서대로 원소가 저장되어 가장 먼저 삽인된 원소는 가장 먼저 삭제 된다.
* 큐의 기본 연산
  * `enQueue`
  * `deQueue`

1. 함수

```python
N = 10
Q = [0] * N
front = rear = -1

def enqueue(item):
    global rear
    # full 체크
    if rear == N - 1:
        return
    rear += 1
    Q[rear] = item

def dequeue():
    global front
    # empty 체크
    if front == rear:
        return
    front += 1
    return Q[front]
```

2.  리스트

```python
Q = []
Q.append(1)
while len(Q) > 0:
	q.pop(0)
```

3.  라이브러리 (Recommended)

```python
from queue import Queue, PriorityQueue
from collections import deque
```

* 잘못된 포화상태 인식

  > 선형 큐를 이용하여 원소의 삽입과 삭제를 계속할 경우, 배열의 앞부분에 활용할 수 있는 공간이 있음에도 불구하고, rear=n-1인 상태 즉 포화상태로 인식하여 더 이상의 삽입을 수행하지 않게 됨

4. 원형 큐

```python
N = 10
Q = [0] * N
front = rear = -1

def enqueue(item):
    global rear
    # full 체크
    if rear == (rear + 1) % N:
        return
    rear = (rear + 1) % N
    Q[rear] = item

def dequeue():
    global front
    # empty 체크
    if front == rear:
        return
    front = (front + 1) % N
    return Q[front]
```

## Priority Queue

> 우선순위를 가진 항목들을 저장하는 큐
>
> FIFO 순서가 아니라 우선순위가 높은 순서대로 먼저 나가게 된다

`적용분야`

> * 시뮬레이션
> * 네트워크 트래픽 제어
> * OS task scheduling
> * Djikstra Algorithm
> * 최소 신장 트리

1. Priority Queue

```python
from queue import PriorityQueue

arr = [ 3, 5, 8, 9, 1, 4, 2, 6 ]
arr2 = [ (3, 5), (2, 5), (1, 8), (0, 9), (2, 1), (3, 4), (2, 1) ]

PQ = PriorityQueue()
for val in arr:
    PQ.put(val)
    
while not PQ.empty():
    print(PQ.get())
    # 기본적으로 오름차순
    

```

2. HeapQueue

```python
from heapq import heappush, heappop

Q = []
arr = [1,3,5,7,9,2,4,6,8,0]

for val in arr:
    heappush(Q, val)
    
while len(Q) > 0:
    print(heappop(Q))
print()
```



# BFS

> 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문하는 방식

* DFS는 방문시 최단경로 보장이 안됨
* BFS는 반드시 최단거리를 알 수 있다.

1. Q에 여러번 들어가기

```python
def bfs(G, V):
    visited = [0] * n 
    queue = deque()
    queue.append(v)
    while queue :
        t = queue.popleft()
        if not visited[t]:
            visited[t] = True
            visit(t)
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
```

2.  Q에는 단 한번씩만 들어가기

```python
from collections import deque
V, E = map(int, input().split())
G = [[] for _ in range(V +1)]

def bfs(s):
    Q = deque()
    visit = [False] * (V + 1) # 1~V 까지
    visit[s] = True; 
    Q.append(s)
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                Q.append(w)
                
    # 큐를 생성, 방문 표시용 빈리스트
    # 시작점을 방문하고 큐에 삽입
    # 빈큐가 아닐 동안
    	# 큐에서 하나 꺼내온다. v
        # v에 방문하지 않은 인접정점을 모두 찾아서
        	# 차례로 방문하고 큐에 삽입

for i in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)
```

```python
from collections import deque
V, E = map(int, input().split())
G = [[] for _ in range(V +1)]
D = [0] * (V + 1) # 최단 거리를 저장
P = [0] * (V + 1) # 최단경로 트리
def bfs(s):
    Q = deque()
    visit = [False] * (V + 1) # 1~V 까지
    visit[s] = True; 
    Q.append(s)
    while Q:
        v = Q.popleft()
        for w in G[v]:
            if not visit[w]:
                visit[w] = True
                D[w] = D[v] + 1
                P[w] = v
                Q.append(w)
```





