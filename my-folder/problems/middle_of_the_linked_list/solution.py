import math

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        len = 1
        curr = head
        while curr.next:
            len += 1
            curr = curr.next

        mid = len // 2 + 1
        i = 1
        while i < mid:
            head = head.next
            i += 1

        return head