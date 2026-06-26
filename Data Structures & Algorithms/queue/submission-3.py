class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def isEmpty(self) -> bool:
        return self.size == 0

    def append(self, value: int) -> None:
        newNode = Node(value, self.tail, self.tail.prev)
        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.size += 1

    def appendleft(self, value: int) -> None:
        newNode = Node(value, self.head.next, self.head)
        self.head.next.prev = newNode
        self.head.next = newNode
        self.size += 1

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        poppedVal = self.tail.prev.val
        beforePop = self.tail.prev.prev
        beforePop.next = self.tail
        self.tail.prev = beforePop
        self.size -= 1
        return poppedVal

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        poppedVal = self.head.next.val
        afterPop = self.head.next.next
        afterPop.prev = self.head
        self.head.next = afterPop
        self.size -= 1
        return poppedVal