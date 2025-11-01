# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def maxDepthRecurse(root) -> int:
            if(root is None):
                return 0
            return max(maxDepthRecurse(root.left), maxDepthRecurse(root.right)) + 1
        return maxDepthRecurse(root)
