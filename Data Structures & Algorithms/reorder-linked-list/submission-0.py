# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr = head
        nodeList = []
        while curr:
            nodeList.append(curr)
            curr = curr.next
        l, r = 0, len(nodeList) - 1
        while l < r:
            nodeList[l].next = nodeList[r]
            l += 1
            if l >= r:
                break
            nodeList[r].next = nodeList[l]
            r -= 1
        nodeList[l].next = None