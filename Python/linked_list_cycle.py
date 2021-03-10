# Leetcode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def detectCycle1(self, head: ListNode) -> ListNode:
        first_ = head
        second = head
        
        while second and second.next:
            first_ = first_.next
            second = second.next.next
            
            if first_ == second:
                second = head
                
                while first_ != second:
                    print(first_.val, second.val)
                    first_ = first_.next
                    second = second.next
                
                return first_
            
            
            
        return None

def detectCycle_slow(self, head: ListNode) -> ListNode:
        node = head
        q = []
        while node != None:
            if q.count(node):
                return node
            
            q.append(node)
            node = node.next
            
            
            
        return None