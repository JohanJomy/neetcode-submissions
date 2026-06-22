# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float('-inf'), float('inf'))
        
    def dfs(self, root, mn, mx):
        if not root:
            return True
        
        if mn >= root.val or root.val >= mx:
            return False
        
        l = self.dfs(root.left, mn, min(mx, root.val))
        r = self.dfs(root.right, max(mn, root.val), mx)

        return l and r