class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        last = self.tail.prev
        new_node = Node(value, last, self.tail)
        last.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        first = self.head.next
        new_node = Node(value, self.head, first)
        first.prev = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        last = self.tail.prev
        poppedVal = last.val
        beforeLast = last.prev

        beforeLast.next = self.tail
        self.tail.prev = beforeLast
        
        return poppedVal

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        first = self.head.next
        poppedVal = first.val
        afterFirst = first.next

        self.head.next = afterFirst
        afterFirst.prev = self.head

        return poppedVal