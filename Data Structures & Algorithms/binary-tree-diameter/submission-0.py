# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.maxval = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.height(root)
        return self.maxval

    def height(self, root):
        if not root:
            return 0

        r = self.height(root.left)
        l = self.height(root.right)

        self.maxval = max(self.maxval, r+l)

        return 1 + max(l, r)
