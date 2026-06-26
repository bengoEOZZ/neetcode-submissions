class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        curr = self.tail.prev

        new_node.next = self.tail
        new_node.prev = curr

        curr.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        curr = self.head.next

        new_node.next = curr
        new_node.prev = self.head

        self.head.next = new_node
        curr.prev = new_node

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