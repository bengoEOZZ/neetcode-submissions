class Node:
    def __init__(self, val, prev=None, next=None):
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
        new_tail = Node(value, self.tail.prev, self.tail)
        before_tail = self.tail.prev

        before_tail.next = new_tail
        self.tail.prev = new_tail

    def appendleft(self, value: int) -> None:
        new_head = Node(value, self.head, self.head.next)
        afterHead = self.head.next

        self.head.next = new_head
        afterHead.prev = new_head

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        popped = self.tail.prev
        poppedVal = popped.val
        beforePopped = popped.prev

        beforePopped.next = self.tail
        self.tail.prev = beforePopped
        return poppedVal

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        popped = self.head.next
        poppedVal = popped.val
        afterPopped = popped.next

        self.head.next = afterPopped
        afterPopped.prev = self.head
        return poppedVal
        
