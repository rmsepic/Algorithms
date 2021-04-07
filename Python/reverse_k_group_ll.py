# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if (head.next is None):
            return head
            
        
        # A -> B -> C -> D -> E
        # k = 3
        prev = first = head     # A
        node = head.next        # B
        next_ = node.next       # C
        i = 1
        
        # Point B to A and hold onto C
        while i < k and node is not None:
            # A -> <- B    C -> D -> E
            # A -> <- B <- C   D -> E
            node.next = prev
            
            # Increment
            prev = node         # prev = B
            node = next_        # node is C
            next_ = next_.next  # next_ is D
            i += 1
            
        ans = prev
        first.next = node
        
        return prev
        
        