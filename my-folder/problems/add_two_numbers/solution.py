# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        extra = 0
        res_head = ListNode(-1)
        curr_res = res_head

        while l1 is not None or l2 is not None or extra != 0:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            temp_sum = val1 + val2 + extra

            temp_sum, extra = self.get_sum_and_extra(temp_sum)

            new_node = ListNode(temp_sum)
            curr_res.next = new_node
            curr_res = new_node

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return res_head.next

    def get_sum_and_extra(self, val):
        if val >= 10:
            return val % 10, val // 10
        return val, 0