# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        def dfs(root):
            nonlocal res
            if root == None:
                return float('-inf')
            
            l = dfs(root.left)
            r = dfs(root.right)

            res = max(res, l + root.val + r, root.val + l, root.val + r, root.val)

            return max(root.val + l, root.val + r, root.val, 0)
        
        dfs(root)
        return res
