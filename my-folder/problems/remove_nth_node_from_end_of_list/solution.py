# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode(0)
        dummy_node.next = head

        first = second = dummy_node
        dist = 0

        while first:
            first = first.next
            if dist == n + 1:
                second = second.next
            else:
                dist += 1
        
        second.next = second.next.next
        return dummy_node.next