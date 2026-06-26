class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class LinkedList:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = self.head
    
    def get(self, index: int) -> int:
        i = 0
        curr = self.head.next
        while curr:
            if i == index:
                return curr.val
            curr = curr.next
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        new_head = Node(val, self.head.next)
        self.head.next = new_head
        if self.head == self.tail:
            self.tail = new_head

    def insertTail(self, val: int) -> None:
        new_tail = Node(val)
        self.tail.next = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head
        while curr and i < index:
            curr = curr.next
            i += 1
        if i == index and curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        return False

    def getValues(self) -> List[int]:
        ans = []
        curr = self.head.next
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans
