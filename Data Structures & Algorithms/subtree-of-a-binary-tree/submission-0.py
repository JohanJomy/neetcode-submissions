# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        if root == None:
            return False

        if self.isequal(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
        

    def isequal(self, root, subRoot):
        if root == subRoot == None:
            return True
        
        if not root and subRoot or root and not subRoot:
            return False
        
        if root.val != subRoot.val:
            return False
        
        return self.isequal(root.left, subRoot.left) and self.isequal(root.right, subRoot.right)