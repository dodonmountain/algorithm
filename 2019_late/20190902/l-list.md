# List

## 리스트

* 순서를 가진 데이터의 집합
  * 순차리스트: 배열 기반 구현
  * 연결 리스트:  메모리 동적할당 기반 구현

```C
#include<stdio.h>
int main{
    int arr[10];
return 0;
}
```

* 시작주소 + (자료형의크기(4byte) * index) 로 접근

* Static => Stack => Heap 메모리 접근

* 단순 배열로 구현하는 경우 자료의 삽입/삭제 연산에 많은 비용이 소모된다.


```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __del__(self):
        print(self.data, '삭제')
class List:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def printlist(self):
        pass
    def insertlast(self, node):
        pass
    def insertfirst(self, node):
        pass
    def
    
```



  

   