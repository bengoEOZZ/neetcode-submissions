# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        indexToRemove = len(nodes) - n
        if indexToRemove == 0:
            return head.next
        nodes[indexToRemove-1].next = nodes[indexToRemove].next
        return head