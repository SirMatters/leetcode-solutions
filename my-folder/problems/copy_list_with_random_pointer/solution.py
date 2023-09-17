"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return 

        curr = head
        while curr:
            duplicate_node = Node(curr.val, curr.next, curr.random)
            curr.next = duplicate_node
            curr = duplicate_node.next

        curr = head.next
        while curr:
            if curr.random:
                curr.random = curr.random.next
            
            if curr.next:
                curr.next = curr.next.next
            curr = curr.next

        return head.next
        

            