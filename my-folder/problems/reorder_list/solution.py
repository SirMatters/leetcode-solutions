# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        mid = self.get_mid_node(head)
        mid_reversed = self.reverse_list(mid)
        head = self.merge_reversed(head, mid_reversed)

    def get_mid_node(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverse_list(self, head):
        prev = None
        curr = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
     
    def merge_reversed(self, head_a, head_b):
        head = head_a
        while head_b.next:
            temp_a = head_a.next
            temp_b = head_b.next
            
            head_a.next = head_b
            head_b.next = temp_a

            head_b = temp_b
            head_a = temp_a
        return head