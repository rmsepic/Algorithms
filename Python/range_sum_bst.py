# Leetcode problem

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST_iterative(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        
        ans = 0
        q = []
        q.append(root)
        
        while q:
            node = q.pop()
            
            if node is None:
                continue
            
            if node.val >= low and node.val <= high:
                ans += node.val
                
                if node.left is not None:
                    q.append(node.left)
                
                if node.right is not None:
                    q.append(node.right)
            elif node.val < low:
                q.append(node.right)
            elif node.val > high:
                q.append(node.left)
                
        return ans
    
    def rangeSumBST_recur(self, root: TreeNode, low: int, high: int) -> int:
        x = y = z = 0
        
        if root is None:
            return 0
        
        if root.val >= low and root.val <= high:
            x = root.val
        
            if root.left is not None:
                y = self.rangeSumBST(root.left, low, high) 

            if root.right is not None:
                z = self.rangeSumBST(root.right, low, high)
        elif root.val < low:
            z = self.rangeSumBST(root.right, low, high)
        elif root.val > high:
            y = self.rangeSumBST(root.left, low, high) 
        
        
        return x + y + z