# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = dummy = ListNode(-1, head)
        curr = r = head
        while curr:
            if n > 0:
                r = r.next
                n -= 1
            else:
                l = l.next
                r = r.next
            curr = curr.next
        l.next = l.next.next
        return dummy.next