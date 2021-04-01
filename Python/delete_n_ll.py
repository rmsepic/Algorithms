# Leetcode problem
# Delete nth node of singly linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # If LL.size == 1
        # Return None because a node has to get deleted
        # Since there is only one delete it
        if (head.next == None):
            return None
        
		# Zero node is a placeholder node that lies behind the head
		# If the LL is 1 => 2 => 3 => 4 => 5, and n = 2 
			#     zero_node     => 1 => 2 => 3 => 4 => 5
			#   ^        ^
			#  goal   point
        zero_node = ListNode()
        zero_node.next = head
        point_node = zero_node   # Node in front n spaces ahead of the goal
        goal_node = zero_node    # The node to be updated (one step behind the node to be deleted)
        
        # Give the point node a lead
		# Zero => 1 => 2 => 3 => 4 => 5
		#   ^               ^
		# goal            point
        for i in range(0, n + 1):
            point_node = point_node.next
        
		# Iterate through the linked list until the last node is found
		
        while (point_node != None):
            point_node = point_node.next
            goal_node = goal_node.next
        
		# Result of the loop
		# Zero => 1 => 2 => 3 => 4 => 5
		#                   ^         ^
		#                   goal      point
        goal_node.next = goal_node.next.next
        
		# Return zero_node.next instead of head in case the head is what gets deleted
        return zero_node.next