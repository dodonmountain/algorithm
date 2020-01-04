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
        if self.head is None:   # 공백 리스트인지 항상 체크
            return
        cur = self.head
        print('[ ', end='')
        while cur is not None:
            print(cur.data, end=' ')
            cur = cur.next
        print(']')

    def insertlast(self, node):
        if self.head is None:   # 빈리스트
            self.head = self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def insertfirst(self, node):
        if self.head is None:
            self.head = self.tail = node

    def deletelast(self):
        if self.head is None:
            return 'error'
        prev, cur = self.head
        while cur.next is not None:
            prev = cur
            cur = cur.next

        if prev is None:
            self.head = self.tail = None
        else:
            prev.next = None
            self.tail = prev

        del cur

        self.size -= 1


    def deletefirst(self):
        if self.head is None:
            return

        cur = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = cur.next

        del cur
        self.size -= 1

    def insertAt(self, idx, node):  # idx: 삽입 위치, node: 삽입 노드
        if self.head is None:
            self.head = self.tail = node
        else:
            prev, cur = None, self.head
            while idx > 0 and cur is not None:
                prev = cur
                cur = cur.next
                idx -= 1

            if prev is None:
                node.next = cur
                self.head = node
            elif cur is None:
                prev.next = node
                self.tail = node
            else:
                node.next = cur
                prev.next = node

    def deleteAt(self, idx):
        pass
