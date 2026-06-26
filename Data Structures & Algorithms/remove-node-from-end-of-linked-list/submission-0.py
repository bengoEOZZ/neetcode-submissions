# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        curr = dummy
        i = 0
        while curr and i < (length-n):
            curr = curr.next
            i += 1
        curr.next = curr.next.next
        return dummy.next