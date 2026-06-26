# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l = dummy = ListNode(-1, head)
        lVal = rVal = 0
        curr = r = head
        while curr:
            if (rVal-lVal) == n:
                l = l.next
                r = r.next
                lVal += 1
                rVal += 1
            else:
                r = r.next
                rVal += 1
            curr = curr.next
        l.next = l.next.next
        return dummy.next