# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(-1)
        curr = head
        while curr:
            new_node = ListNode(curr.val, dummyNode.next)
            dummyNode.next = new_node
            print(curr.val)
            curr = curr.next
        return dummyNode.next