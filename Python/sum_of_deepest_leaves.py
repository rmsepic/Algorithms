# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class DeepestLeaves:    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        depth = findDepth(root, 0)
        print(depth)
        
        q = [] # Hold the valid nodes
        q.append(root)
        
        for n in range(0, depth):
            cur_len = len(q)
            for i in range(0, cur_len):
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                
                if node.right:
                    q.append(node.right)
        
        ans = 0
        for n in q:
            ans += n.val
            
        return ans
    
def findDepth(node: TreeNode, depth: int) -> int:
    if node.left and node.right:
        return max(findDepth(node.left, depth + 1), findDepth(node.right, depth + 1))
    elif node.left:
        return findDepth(node.left, depth + 1)
    elif node.right:
        return findDepth(node.right, depth + 1)

    # If node.left and node.right are both NULL
    return depth