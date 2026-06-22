# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 0 0 
        if p == None and q == None:
            return True

        # 1 0 or 0 1
        if p and not q or not p and q:
            return False
        
        if p.val != q.val:
            return False
        
        # both p and q exists
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        
