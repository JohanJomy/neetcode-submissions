# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1
        ctr = 0

        def dfs(root):
            nonlocal ctr, res
            if not root:
                return

            dfs(root.left)

            ctr += 1

            if ctr == k:
                res = root.val
            
            dfs(root.right)
        
        dfs(root)
        return res
            


            
            

        

