"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashCopy = {}
        curr = head
        while curr:
            hashCopy[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            hashCopy[curr].next = hashCopy[curr.next] if curr.next else None
            hashCopy[curr].random = hashCopy[curr.random] if curr.random else None
            curr = curr.next
        return hashCopy[head] if head else None