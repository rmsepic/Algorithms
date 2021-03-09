# Leetcode problem

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        queue1 = queue2 = []
        queue1.append(p)
        queue2.append(q)
        
        while len(queue1) != 0 and len(queue2) != 0:
            node1 = queue1.pop()
            node2 = queue2.pop()
            
            if node1 is not None and node2 is None:
                return False
            elif node1 is None and node2 is not None:
                return False
            
            if node1 is not None and node2 is not None:
                if node1.val == node2.val:
                    queue1.append(node1.left)
                    queue2.append(node2.left)
                    queue1.append(node1.right)
                    queue2.append(node2.right)
                else:
                    return False
            
        return True