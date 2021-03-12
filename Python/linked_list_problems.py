# Leetcode Problems involving linked lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def detectCycle1(head: ListNode) -> ListNode:
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

def detectCycle_slow(head: ListNode) -> ListNode:
        node = head
        q = []
        while node != None:
            if q.count(node):
                return node
            
            q.append(node)
            node = node.next
            
            
            
        return None

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next

def reverseList(head: ListNode) -> ListNode:
    if head == None:
        return head
    
    q = []
         
    node = head
    while node is not None:
        q.append(node)
        node = node.next
    
    new_head = q[-1]
    
    while q:
        node = q.pop()
        if len(q) > 0:
            node.next = q[-1]
        else:
            # New ending node
            node.next = None
        
    return new_head