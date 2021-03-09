# Leetcode problem

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        diam = 0
        max_ = 0
        dic = {None: 0}
        q = []
        q.append(root)
        
        while q:
            node = q.pop()
            
            if node is None:
                continue
            
            left = dic.get(node.left)
            right = dic.get(node.right)
            
            if left == None or right == None:         
                q.append(node)
                q.append(node.left)
                q.append(node.right)
            else:    
                diam = max(left, right) + 1
                max_ = max(left + right, max_) 
                    
                dic.update({node: diam})
                
                
        
        return max_