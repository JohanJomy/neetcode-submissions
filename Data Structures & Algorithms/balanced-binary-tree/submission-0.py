# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def checkHeight(self, root):
        if root == None:
            return 0

        l = self.checkHeight(root.left)
        r = self.checkHeight(root.right)

        # print(root.val, l, r, l == False, r == False)
        if l == -1 or r == -1:
            return -1

        if abs(l-r) <= 1:
            print(root.val, max(l, r) + 1)
            return max(l, r) + 1
        else:
            return -1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if self.checkHeight(root) == -1:
            return False
        return True
        
