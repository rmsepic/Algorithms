# Leetcode problem


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def symmetric(self, left: TreeNode, right: TreeNode) -> bool:
        if left is None and right is None:
            return True
        elif left != None and right != None and left.val == right.val:
            return self.symmetric(left.left, right.right) and self.symmetric(left.right, right.left)
        else:
            return False
        
    
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.symmetric(root.left, root.right)
        